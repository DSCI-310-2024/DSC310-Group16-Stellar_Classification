import os
import sys
from pathlib import Path

import click
import pandas as pd

# Import clean_confidence_intervals function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from clean_confidence_intervals import clean_confidence_intervals


@click.command()
@click.option("--input_file", type=str, default="data/raw/planet-systems.csv")
@click.option("--output_file", type=str, default="data/processed/planet-systems.csv")
def clean_data(input_file, output_file):
    """
    Reads data from the input file, performs data cleaning and preprocessing,
    and saves the cleaned data to the output file.
    """
    print("### Cleaning and preprocessing dataset... ###")
    os.makedirs(Path(output_file).parent, exist_ok=True)

    # Reads data from the input file
    exoplanet_data = pd.read_csv(input_file)

    # Drop the rows with NA values
    exoplanet_data = exoplanet_data.dropna(
        subset=["st_spectype", "sy_umag", "sy_gmag", "sy_rmag", "sy_imag", "sy_zmag"]
    )

    # Removes confidence intervals, keeping only the mean value (functions imported from src folder)
    exoplanet_data = clean_confidence_intervals(exoplanet_data)

    # Iterates through the columns and renames columns by removing 'str' from the end of column names.
    for col in exoplanet_data.columns:
        if col.endswith("str"):
            new_col_name = col[:-3]  # removes "str"
            exoplanet_data.rename(columns={col: new_col_name}, inplace=True)

    # Filters the data to keep only the rows where the values in the "st_spectype" column are among
    # the specified spectral types: "O", "B", "A", "F", "G", "K", or "M" and converts spectral type
    # column to category type.
    exoplanet_data = exoplanet_data.copy()  # needed to avoid warning raised by pandas
    exoplanet_data["st_spectype"] = exoplanet_data["st_spectype"].transform(
        lambda x: x[0]
    )
    exoplanet_data = exoplanet_data.loc[
        exoplanet_data["st_spectype"].isin(["O", "B", "A", "F", "G", "K", "M"])
    ]
    exoplanet_data["st_spectype"] = exoplanet_data["st_spectype"].astype("category").round(2)

    # Saves the cleaned and preprocessed data to the output file
    exoplanet_data.to_csv(output_file, index=False)

    print("Data cleaned and saved to:", output_file)


if __name__ == "__main__":
    clean_data()
