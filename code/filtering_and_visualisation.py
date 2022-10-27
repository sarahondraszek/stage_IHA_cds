import os.path
import random
import warnings

import matplotlib.pyplot as plt
import pandas as pd
from ipynb.fs.full.merge_spreadsheets import merge_files
from pandas.core.common import SettingWithCopyWarning

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

PATH_ORIGINAL_INPUT: str = '../data/cds_sheets/*'
PATH_MERGED_SPREADSHEET: str = '../data/merged/merged_cds_spreadsheet.csv'
CDS_GND: str = 'http://d-nb.info/gnd/116765968'

FILTER_QUERIES: dict = {'gnd_sender': 'GND (Verfasser)',
                        'reference': 'Verweise',
                        'template': 'Vorlage',
                        'decade': 'decade',
                        'addressee': 'Empfänger'
                        }

if not os.path.isfile(PATH_MERGED_SPREADSHEET):
    DATA = merge_files(PATH_ORIGINAL_INPUT)
else:
    DATA = pd.read_csv(PATH_MERGED_SPREADSHEET)

DATA = DATA.drop(DATA.columns[[0]], axis=1)


def filter_data(input_data: pd.DataFrame = DATA, filter_query=None) -> pd.DataFrame:
    """
    Filtering input data from merged spreadsheets according to given filter queries.
    :param input_data: Merged dataframe.
    :param filter_query: Query that can be used to filter the dataframe.
    :return: Filtered dataframe.
    """

    if filter_query is None:
        filter_query = FILTER_QUERIES

    # Adding decades to dataframe by extracting the years from the letter's dates.
    input_data['year'] = pd.DatetimeIndex(input_data['Datierung (JJJJ-MM-TT)']).year
    input_data['decade'] = (10 * (input_data['year'] // 10))
    input_data['decade'] = input_data['decade'].astype('Int64')

    # Replacing NaN values with zeros for facilitated filtering.
    input_data['Verweise'] = input_data['Verweise'].fillna(0)
    # Filtering: Output of only letters from CdS that are originals.
    filtered_df = input_data.loc[
        (input_data[filter_query['gnd_sender']] == CDS_GND)
        &
        (input_data[filter_query['reference']] == 0)
        &
        (
            (input_data[filter_query['template']] == 'Abschrift')
            |
            (input_data[filter_query['template']] == 'Original')
        )
    ]

    return filtered_df


def visualise_histogram(input_data: pd.DataFrame) -> None:
    """
    Histogram of correspondence frequencies throughout the decades. Can be adapted according to visualisation goals.
    :param input_data:
    :return:
    """
    # Histogram of all correspondences throughout the decades.
    grouped_all = input_data.groupby(FILTER_QUERIES['decade']).count().reset_index()

    plt.bar(
        grouped_all[FILTER_QUERIES['decade']],
        grouped_all['FuD-Key']
    )

    plt.savefig('../data/vis/decades_freq.png')

    # Histogram of correspondences with addressees throughout the decades.
    # TO-DO:
    # - Get it working correctly so that I can make the frequencies the weights in the network.
    # - Why does pandas' .groupby() delete duplicate rows?
    grouped_addressees = input_data.groupby(
        [FILTER_QUERIES['decade'],
         FILTER_QUERIES['addressee']]
    ).count().reset_index()

    input_data['Count'] = 1
    input_data.value_counts(
        ['Verfasser',
         FILTER_QUERIES['decade'],
         FILTER_QUERIES['addressee']]
    ).reset_index(name='counts').to_csv('../data/retrieved/network_data.csv')

    colour = [
        "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        for _ in range(len(set(grouped_addressees[FILTER_QUERIES['decade']])))
    ]

    i = 0
    for decade in set(grouped_addressees[FILTER_QUERIES['decade']]):
        plt.clf()
        plt.bar(
            grouped_addressees.loc[grouped_addressees[FILTER_QUERIES['decade']] == decade][FILTER_QUERIES['addressee']],
            grouped_addressees.loc[grouped_addressees[FILTER_QUERIES['decade']] == decade]['FuD-Key'],
            color=colour[i]
        )

        plt.title(decade)
        plt.xticks(rotation='vertical')
        plt.savefig('../data/vis/decade_' + str(decade) + '.png', bbox_inches="tight")
        i += 1


FILTERED_DF_CDS = filter_data()
FILTERED_DF_CDS.to_csv('../data/retrieved/filtered_cds_data.csv')

visualise_histogram(FILTERED_DF_CDS)