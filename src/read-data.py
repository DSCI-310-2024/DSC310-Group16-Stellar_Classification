import glob
import os
from datetime import datetime

import click
import pandas as pd
import requests
from traitlets import default


# parse/define command line arguments here
@click.command()
@click.option('--url', type=str)
@click.option('--output_path', type=str)
def fetch_data(url, output_path):
    """Download the data from the internet or read in the data from disk if it exists.

    Documentation for constructing a TPA call to retrieve the dataset:
    https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS

    Returns
        df: DataFrame
    """
    current_date = datetime.now().date().strftime("%Y-%m-%d")

    dataset_name = "planet-systems"
    raw_data_dir = os.path.join("data", "raw")
    default_out_path = os.path.join(raw_data_dir, f"{current_date}_{dataset_name}.csv")
    raw_data_path = output_path or default_out_path

    # make directory where we store our raw data
    os.makedirs(raw_data_dir, exist_ok=True)

    # check if we already have the dataset downloaded
    folder_not_empty = len(os.listdir(raw_data_dir)) != 0
    raw_data_files = glob.glob(f"{raw_data_dir}/*{dataset_name}*")
    if len(raw_data_files) > 0:
        last_download_date = raw_data_files[0].split("_")[0].split("/")[-1]
    else :
        last_download_date = "0-0-0"
    data_up2date = last_download_date == current_date

    if folder_not_empty and data_up2date:
        print(len(os.listdir(raw_data_dir)))
        print(f"Using already existing dataset under {raw_data_dir}")
    else:
        # remove outdated dataset file
        [os.remove(file) for file in raw_data_files]

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

        print(f"Downloading Planet Systems dataset from {url}")

        response = requests.get(url)

        # assume request was successfull and access the downloaded content    
        raw_data = response.content

        # write downloaded content into a file under the raw data directory
        with open(raw_data_path, "wb") as f:
            f.write(raw_data)

    # df holds the expolanet dataset as a DataFrame object
    df = pd.read_csv(raw_data_path)

    # remove confidence interval from all cells, just keep the mean value for these
    df = df.apply(lambda col: col.str.split('&').str[0])

    print("Successfully loaded the dataset.")

    return df


if __name__ == "__main__":
    exoplanet_data = fetch_data() # pass any command line args to main here