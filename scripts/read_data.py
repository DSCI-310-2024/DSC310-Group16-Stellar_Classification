import os

import click
from classifyspectraltype import fetch_data


@click.command()
@click.option("--url", type=str)
@click.option("--output_path", type=str)
def read_data(url, output_path):
    """
    Provides a command-line interface to download and store exoplanet data.
    It uses predefined columns to fetch data from a specified URL and save it to a given
    output path. The script prints updates about its execution status and returns the
    downloaded dataset as a pandas DataFrame.
    """
    print(f"### Running {os.path.basename(__file__)} ###")

    # define the columns we want do keep in the dataset
    columns = [
        "pl_name",
        "st_spectype",
        "sy_umag",
        "sy_gmag",
        "sy_rmag",
        "sy_imag",
        "sy_zmag",
    ]

    # download the dataset
    exoplanet_data = fetch_data(base_url=url, output_path=output_path, columns=columns)

    print(f"### Successfully ran {os.path.basename(__file__)} ###")
    return exoplanet_data


if __name__ == "__main__":
    read_data()
