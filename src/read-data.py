import click
import os
from datetime import datetime
import requests
import pandas as pd
# parse/define command line arguments here
@click.command()
@click.option('--url', type=str)
@click.option('--output', type=str)

# define main function
def main(url, output):
    current_date = datetime.now().date().strftime("%Y-%m-%d")

    # raw_data_dir = os.path.join("data")
    # raw_data_path = os.path.join(raw_data_dir, f"{current_date}_planet-systems.csv")
    # make directory where we store our raw data
    #os.makedirs(raw_data_dir, exist_ok=True)

    # check if we already have the dataset downloaded
    if len(os.listdir(raw_data_dir)) != 0:
        print(len(os.listdir(raw_data_dir)))
        print(f"Using already existing dataset under {raw_data_dir}")
    else:
        # download the raw data as CSV under the raw data directory
        #url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/IceTable/nph-iceTblDownload"
        
        print(f"Downloading Planet Systems dataset from {url}")

        # define an HTTP request
        payload = {
            "workspace": "2024.02.29_21.58.35_020450/TblView/2024.03.02_14.52.28_004142",
            "useTimestamp": "1",
            "table": "/exodata/kvmexoweb/ExoTables/PS.tbl",
            "format": "CSV",
            "user": "",
            "label": "*",
            "columns": "pl_name_display,st_spectype,sy_umagstr,sy_gmagstr,sy_rmagstr,sy_imagstr,sy_zmagstr",
            "rows": "both",
            "mission": "ExoplanetArchive"
        }
        response = requests.get(url, params=payload)

        # assume request was successfull and access the downloaded content    
        raw_data = response.content

        # write downloaded content into a file under the raw data directory
        with open(output, "wb") as f:
            f.write(raw_data)

    # df holds the expolanet dataset as a DataFrame object
    df = pd.read_csv(
        output,
        header = 23, # 24-1=23
        dtype = {'pl_name' : 'string', 'st_spectype' : 'string'}
    )

    # remove columns in the dataset that have 'err' in their name
    filtered_columns = [col for col in df.columns if 'err' not in col]

    exoplanet_data = df[filtered_columns]


if __name__ == "__main__":
    main() # pass any command line args to main here