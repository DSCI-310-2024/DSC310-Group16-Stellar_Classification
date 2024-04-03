import os
from pathlib import Path
import click
import pandas as pd
from src.clean_preprocess_data import clean_confidence_intervals
from src.clean_preprocess_data import rename_columns
from src.clean_preprocess_data import filter_and_categorize_spectral_types


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

    # Cleans and preprocesses data
    exoplanet_data = clean_confidence_intervals(exoplanet_data)
    exoplanet_data = rename_columns(exoplanet_data)
    exoplanet_data = filter_and_categorize_spectral_types(exoplanet_data)
    
    # Saves the cleaned and preprocessed data to the output file
    exoplanet_data.to_csv(output_file, index=False)

    print("Data cleaned and saved to:", output_file)


if __name__ == "__main__":
    clean_data()