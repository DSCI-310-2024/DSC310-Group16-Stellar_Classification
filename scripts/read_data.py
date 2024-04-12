import os

import click

from src.fetch_exoplanet_dataset import fetch_data


@click.command()
@click.option("--url", type=str)
@click.option("--output_path", type=str)
def read_data(url, output_path):
    print(f"### Running {os.path.basename(__file__)} ###")

    # define the columns we want do keep in the dataset
    columns = (
        "pl_name," "st_spectype," "sy_umag," "sy_gmag," "sy_rmag," "sy_imag," "sy_zmag"
    )

    # download the dataset
    exoplanet_data = fetch_data(url=url, output_path=output_path, columns=columns)

    print(f"### Successfully ran {os.path.basename(__file__)} ###")
    return exoplanet_data


if __name__ == "__main__":
    read_data()
