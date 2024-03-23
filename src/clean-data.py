import os
from pathlib import Path
import click
import pandas as pd


@click.command()
@click.option("--input_file", type=str, default="data/raw/planet-systems.csv")
@click.option("--output_file", type=str, default="data/processed/planet-systems.csv")
def clean_data(input_file, output_file):
    """
    Reads data from the input file, performs data cleaning, and saves the cleaned data 
    to the output file.
    """
    print("### Cleaning and preprocessing dataset... ###")
    os.makedirs(Path(output_file).parent, exist_ok=True)
    # Read the data from the input file
    exoplanet_data = pd.read_csv(input_file)

    # 1) remove confidence interval from all cells, just keep the mean value for these
    exoplanet_data = exoplanet_data.apply(lambda col: col.str.split("&").str[0])

    # iterate through the columns and rename if "str" is at the end of the column name
    for col in exoplanet_data.columns:
        if col.endswith("str"):
            new_col_name = col[:-3]  # remove "str"
            exoplanet_data.rename(columns={col: new_col_name}, inplace=True)

    # Drop the rows with NA values
    only_stars_data = exoplanet_data.dropna(
        subset=["st_spectype", "sy_umag", "sy_gmag", "sy_rmag", "sy_imag", "sy_zmag"]
    )

    # Created column names with proper spectral type
    only_stars_data_copy = (
        only_stars_data.copy()
    )  # needed to avoid warning raised by pandas
    only_stars_data_copy["st_spectype"] = only_stars_data_copy["st_spectype"].transform(
        lambda x: x[0]
    )
    only_stars_data_copy = only_stars_data_copy.loc[
        only_stars_data_copy["st_spectype"].isin(["O", "B", "A", "F", "G", "K", "M"])
    ]
    only_stars_data_copy["st_spectype"] = only_stars_data_copy["st_spectype"].astype(
        "category"
    )

    # Save the cleaned data to the output file
    only_stars_data_copy.to_csv(output_file, index=False)

    print("Data cleaned and saved to:", output_file)


if __name__ == "__main__":
    clean_data()
