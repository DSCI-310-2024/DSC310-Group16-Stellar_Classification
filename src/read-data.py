import glob
import os
from datetime import datetime
from pathlib import Path

import click
import pandas as pd
import requests

def fetch_data(url, output_path) -> pd.DataFrame:
    """Download the data from the internet or read in the data from disk if it exists.

    The dataset is saved under data/raw/Y-M-D_planet-systems.csv,
    along with its processed version under data/processed/planet-systems.csv.

    Documentation for constructing a TPA call to retrieve the dataset:
    https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS
    """
    dataset_name = "planet-systems"
    raw_data_dir = Path("data") / "raw"
    default_out_path = raw_data_dir / f"{dataset_name}.csv"
    raw_data_path = output_path or default_out_path

    # make directory where we store our raw data
    os.makedirs(raw_data_dir, exist_ok=True)

    # download the raw data as CSV under the raw data directory using a TPA query
    base_url = "https://exoplanetarchive.ipac.caltech.edu"
    columns = (
        "pl_name,"
        "st_spectype,"
        "sy_umagstr,"
        "sy_gmagstr,"
        "sy_rmagstr,"
        "sy_imagstr,"
        "sy_zmagstr"
    )
    query = f"select+{columns}+from+ps"
    format = "csv"
    url = url or f"{base_url}/TAP/sync?query={query}&format={format}"

    print(f"Downloading Planet Systems dataset from {url}\nunder {raw_data_path}")

    response = requests.get(url)

    # assume request was successfull and access the downloaded content
    raw_data = response.content

    # write downloaded content into a file under the raw data directory
    with open(raw_data_path, "wb") as f:
        f.write(raw_data)

    # df holds the expolanet dataset as a DataFrame object
    df = pd.read_csv(raw_data_path)

    print(f"Loaded dataset from {raw_data_path}")

    return df


@click.command()
@click.option("--url", type=str)
@click.option("--output_path", type=str)
def read_data(url, output_path):
    print(f"### Running {os.path.basename(__file__)} ###")

    exoplanet_data = fetch_data(url, output_path)

    print(f"### Successfully ran {os.path.basename(__file__)} ###")
    return exoplanet_data


if __name__ == "__main__":
    read_data()
