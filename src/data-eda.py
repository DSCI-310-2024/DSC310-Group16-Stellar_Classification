# This script will create a PNG for our star count as well as the tables and corresponding box plots 
# of the magnitudes of bands for each star

# Imports
import os
import click
import pandas as pd
import matplotlib.pyplot as plt

# Main function 
@click.command()
@click.argument('cleaned_input_data', type=str, default="data/processed/planet-systems.csv")
@click.argument('eda_png_dir', type=str, default="results/figures")
@click.argument('eda_csv_dir', type=str, default="results/figures")
@click.argument('box_plot_dir', type=str, default="results/figures")
def main(cleaned_input_data, eda_png_dir, eda_csv_dir, box_plot_dir):
    # create dirs if they don't exist
    dirs = [eda_png_dir, eda_csv_dir, box_plot_dir]
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)

    #read data from cleaned data file
    data = pd.read_csv(f'{cleaned_input_data}')

    #store the value counts as a DataFrame
    types_summ = pd.DataFrame(data["st_spectype"].value_counts())

    #create and save the histogram
    fig, ax = plt.subplots(1, 1)
    types_summ.plot.bar(xlabel = 'Stellar classification', title="Counts of type of stars", ax=ax)

    for col in types_summ.columns:
        for id, val in enumerate(types_summ[col]):
            ax.text(id, val, str(val))

    plt.savefig(f'{eda_png_dir}/star_count_hist.png')

    #create and save the table for sy_umag
    sy_umag_csv = (data[['st_spectype', 'sy_umag']].groupby('st_spectype').describe())
    sy_umag_csv.to_csv(f'{eda_csv_dir}/sy_umag.csv')

    #create and save the boxplot for sy_umag
    sy_umag_bp = data[['st_spectype', 'sy_umag']].groupby('st_spectype').boxplot()
    plt.savefig(f'{box_plot_dir}/sy_umag.png')


    #create and save the table for sy_gmag
    sy_gmag_csv = (data[['st_spectype', 'sy_gmag']].groupby('st_spectype').describe())
    sy_gmag_csv.to_csv(f'{eda_csv_dir}/sy_gmag.csv')

    #create and save the boxplot for sy_gmag
    sy_gmag_bp = data[['st_spectype', 'sy_gmag']].groupby('st_spectype').boxplot()
    plt.savefig(f'{box_plot_dir}/sy_gmag.png')


    #create and save the table for sy_rmag
    sy_rmag_csv = (data[['st_spectype', 'sy_rmag']].groupby('st_spectype').describe())
    sy_rmag_csv.to_csv(f'{eda_csv_dir}/sy_rmag.csv')

    #create and save the boxplot for sy_rmag
    ry_gmag_bp = data[['st_spectype', 'sy_rmag']].groupby('st_spectype').boxplot()
    plt.savefig(f'{box_plot_dir}/sy_rmag.png')


    #create and save the table for sy_imag
    sy_imag_csv = (data[['st_spectype', 'sy_imag']].groupby('st_spectype').describe())
    sy_imag_csv.to_csv(f'{eda_csv_dir}/sy_imag.csv')

    #create and save the boxplot for sy_imag
    sy_imag_bp = data[['st_spectype', 'sy_imag']].groupby('st_spectype').boxplot()
    plt.savefig(f'{box_plot_dir}/sy_imag.png')


    #create and save the table for sy_zmag
    sy_zmag_csv = (data[['st_spectype', 'sy_zmag']].groupby('st_spectype').describe())
    sy_zmag_csv.to_csv(f'{eda_csv_dir}/sy_zmag.csv')

    #create and save the boxplot for sy_zmag
    sy_zmag_bp = data[['st_spectype', 'sy_zmag']].groupby('st_spectype').boxplot()
    plt.savefig(f'{box_plot_dir}/sy_zmag.png')

if __name__ == '__main__':
    main() 
