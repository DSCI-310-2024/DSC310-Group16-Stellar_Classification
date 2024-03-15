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
    
    # Check for and drop duplicate rows
    duplicates = data[data.duplicated()]
    data.drop_duplicates(inplace=True)
    
    # Drop the 'OperatingSystems' column
    data.drop(columns=["OperatingSystems"], inplace=True)
    
    # Save the cleaned data to the output file
    data.to_csv(output_file, index=False)
    
    click.echo("Data cleaned and saved to:", output_file)

if __name__ == "__main__":
    clean_data()
