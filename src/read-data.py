import glob
import os
from datetime import datetime
from pathlib import Path

import click
import pandas as pd
import requests


def dataset_is_up2date(dataset_dir, dataset_name) -> bool:
    """Check if dataset is up to date, meaning it was downloaded today."""
    current_date = datetime.now().date().strftime("%Y-%m-%d")
    raw_data_files = glob.glob(f"{dataset_dir}/*{dataset_name}*")

    if len(raw_data_files) > 0:
        last_download_date = raw_data_files[0].split("_")[0].split("/")[-1]
    else :
        last_download_date = "0-0-0"

    return last_download_date == current_date

def remove_outdated_files(dataset_dir, dataset_name) -> list[str]:
    """Remove outdated files that have the substring `dataset_name` in them."""
    files = glob.glob(f"{dataset_dir}/*{dataset_name}*")
    [os.remove(file) for file in files]
    print(f"Removed outdated files:\n{files}") if len(files) > 0 else None
    return files


def fetch_data(url, output_path) -> pd.DataFrame:
    """Download the data from the internet or read in the data from disk if it exists.

    The dataset is saved under data/raw/Y-M-D_planet-systems.csv.

    Documentation for constructing a TPA call to retrieve the dataset:
    https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS
    """
    current_date = datetime.now().date().strftime("%Y-%m-%d")

    dataset_name = "planet-systems"
    raw_data_dir = Path("data") / "raw"
    default_out_path = raw_data_dir / f"{current_date}_{dataset_name}.csv"
    raw_data_path = output_path or default_out_path

    # make directory where we store our raw data
    os.makedirs(raw_data_dir, exist_ok=True)

    if not dataset_is_up2date(raw_data_dir, dataset_name):
        remove_outdated_files(raw_data_dir, dataset_name)

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

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Carry out some basic preprocessing steps on the dataset.

    The dataset is saved under data/processed/Y-M-D_planet-systems.csv
    
    Returns
        df: DataFrame
    """
    current_date = datetime.now().date().strftime("%Y-%m-%d")
    dataset_name = "planet-systems"
    dataset_dir = Path("data") / "processed"
    dataset_path = dataset_dir / f"{current_date}_planet-systems.csv"

    if dataset_is_up2date(dataset_dir, dataset_name):
        print(f"Loaded dataset from {dataset_path}")
        return df

    remove_outdated_files(dataset_dir, dataset_name)

    print("Preprocessing dataset...")

    # 1) remove confidence interval from all cells, just keep the mean value for these
    df = df.apply(lambda col: col.str.split('&').str[0])

    # write dataframe as a csv file under data_path
    df.to_csv(dataset_path, index=False)

    print(f"Saved dataset under {dataset_path}")

    return df


@click.command()
@click.option('--url', type=str)
@click.option('--output_path', type=str)
def read_data(url, output_path):
    print(f"### Running {os.path.basename(__file__)} ###")
    exoplanet_data = preprocess(fetch_data(url, output_path))
    print(f"### Successfully ran {os.path.basename(__file__)} ###")
    return exoplanet_data

if __name__ == "__main__":
    read_data()