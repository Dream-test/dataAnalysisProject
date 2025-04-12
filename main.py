from pprint import pprint

import requests
import pandas as pd
import matplotlib.pyplot as plt
from six import StringIO


def get_data_frame(url):
    response = requests.get(url)
    return pd.read_csv(StringIO(response.text))

if __name__ == '__main__':
    url  = "https://sdmx.oecd.org/public/rest/data/OECD.ECO.MPD,DSD_AN_HOUSE_PRICES@DF_HOUSE_PRICES,1.0/.Q.RPI+RHP.?startPeriod=2000-Q1&format=csvfile"

    df = get_data_frame(url)
    clean_df = df[["REF_AREA", "TIME_PERIOD", "OBS_VALUE"]]
    grouped = clean_df.groupby("REF_AREA")["OBS_VALUE"].mean().sort_values(ascending=False)

    pprint(grouped)

    # Graph plotting
    plt.figure(figsize=(10, 5))
    grouped.plot(kind="bar")
    plt.title("Среднее значение OBS_VALUE по REF_AREA")
    plt.xlabel("REF_AREA")
    plt.ylabel("Среднее OBS_VALUE")
    plt.grid(axis="y")
    plt.tight_layout()

    # Displaying the graph
    plt.show()
