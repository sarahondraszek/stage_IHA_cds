import re

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

CDS_GND = "1161012168"
GND_LINK = "http://d-nb.info/gnd/"
GEONAMES_LINK = "https://www.geonames.org/"


def data_retrieval(input_path: str = "./data/correspondance.xlsx") -> (pd.DataFrame, pd.DataFrame):
    # Retrieve all data with geo information
    df = pd.read_excel(input_path)
    # Retrieve only data about CDS
    cds_df = df[df["senderID"] == GND_LINK + CDS_GND]

    return df, cds_df




#def visualisation():
