import os

import pandas as pd
import glob
import re
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


def merge_files(path: str) -> pd.DataFrame:
    """
    Merging existing files with data from the CdS correspondence
    into one spreadsheet for further visualisation purposes.

    :param path: File path of directory.
    :return: None.
    """

    csv_input: pd.DataFrame
    excel_input: pd.DataFrame

    # Checking format of file (CSV or XLSX) and parsing the data accordingly:
    for file in glob.glob(path):
        if os.path.basename(file).endswith('xlsx'):
            print(os.path.basename(file))
            excel_input = pd.read_excel(file)
        elif os.path.basename(file).endswith('csv'):
            print(os.path.basename(file))
            # csv_input = pd.read_csv(file)

        # print(csv_input.head())

    return excel_input
