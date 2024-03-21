import click
import pandas as pd

@click.command()
@click.argument('input_file', type=str)
@click.argument('output_file', type=str)

def clean_data(input_file, output_file):
    """
    Reads data from the input file, performs data cleaning, and saves the cleaned data to the output file.
    """
    # Read the data from the input file
    data = pd.read_csv(input_file)
    
    # Drop the rows with NA values
    only_stars_data = exoplanet_data.dropna(subset = ['st_spectype',
                                                  'sy_umag',
                                                  'sy_gmag',
                                                  'sy_rmag',
                                                  'sy_imag',
                                                  'sy_zmag'])
    
    # Created column names with proper spectral type
    only_stars_data_copy = only_stars_data.copy() # needed to avoid warning raised by pandas
    only_stars_data_copy["st_spectype"] = only_stars_data_copy['st_spectype'].transform(lambda x: x[0])
    only_stars_data_copy = only_stars_data_copy.loc[only_stars_data_copy['st_spectype'].isin(['O','B', 'A', 'F', 'G', 'K', 'M'])]
    only_stars_data_copy["st_spectype"] = only_stars_data_copy["st_spectype"].astype("category")

    # Save the cleaned data to the output file
    only_stars_data_copy.to_csv(output_file, index=False)
    
    click.echo("Data cleaned and saved to:", output_file)

if __name__ == "__main__":
    clean_data()

# Are we dropping NAs???
