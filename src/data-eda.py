# This script will create a PNG, and the tables and corresponding box plots 
# of the magnitudes of bands for each star

# Imports
import click
import pandas as pd
import matplotlib.pyplot as plt

# Main function 
@click.command()
@click.argument('cleaned_data', type=str)
@click.argument('eda_png', type=str)
@click.argument('csv_folder', type=str)
@click.argument('box_plot_folder', type=str)


def main():

    #read data from cleaned data file
    data = pd.read_csv(cleaned_data)

    #store the value counts as a DataFrame
    types_summ = pd.DataFrame(data["st_spectype"].value_counts())

    #create and save the histogram
    fig, ax = plt.subplots(1, 1)
    types_summ.plot.bar(xlabel = 'Stellar classification', title="Counts of type of stars", ax=ax)
    
    for col in types_summ.columns:
        for id, val in enumerate(types_summ[col]):
            ax.text(id, val, str(val))

    plt.savefig(f'{eda_png}/star_count_hist.png')

    #create and save the table for sy_umag
    sy_umag_csv = (data[['st_spectype', 'sy_umag']].groupby('st_spectype').describe())
    sy_umag_csv.to_csv(f'{csv_folder}/sy_umag.csv')

    #create and save the boxplot for sy_umag
    sy_umag_bp = data[['st_spectype', 'sy_umag']].groupby('st_spectype').boxplot()
    sy_umag_bp.save_fig(f'{box_plot_folder}/sy_umag.png')


    #create and save the table for sy_gmag
    sy_gmag_csv = (data[['st_spectype', 'sy_gmag']].groupby('st_spectype').describe())
    sy_gmag_csv.to_csv(f'{csv_folder}/sy_gmag.csv')

    #create and save the boxplot for sy_gmag
    sy_gmag_bp = data[['st_spectype', 'sy_gmag']].groupby('st_spectype').boxplot()
    sy_gmag_bp.save_fig(f'{box_plot_folder}/sy_gmag.png')


    #create and save the table for sy_rmag
    sy_rmag_csv = (data[['st_spectype', 'sy_rmag']].groupby('st_spectype').describe())
    sy_rmag_csv.to_csv(f'{csv_folder}/sy_rmag.csv')

    #create and save the boxplot for sy_rmag
    ry_gmag_bp = data[['st_spectype', 'sy_rmag']].groupby('st_spectype').boxplot()
    ry_gmag_bp.save_fig(f'{box_plot_folder}/sy_rmag.png')


    #create and save the table for sy_imag
    sy_imag_csv = (data[['st_spectype', 'sy_imag']].groupby('st_spectype').describe())
    sy_imag_csv.to_csv(f'{csv_folder}/sy_imag.csv')

    #create and save the boxplot for sy_imag
    sy_imag_bp = data[['st_spectype', 'sy_imag']].groupby('st_spectype').boxplot()
    sy_imag_bp.save_fig(f'{box_plot_folder}/sy_imag.png')


    #create and save the table for sy_zmag
    sy_zmag_csv = (data[['st_spectype', 'sy_zmag']].groupby('st_spectype').describe())
    sy_zmag_csv.to_csv(f'{csv_folder}/sy_zmag.csv')

    #create and save the boxplot for sy_zmag
    sy_zmag_bp = data[['st_spectype', 'sy_zmag']].groupby('st_spectype').boxplot()
    sy_zmag_bp.save_fig(f'{box_plot_folder}/sy_zmag.png')

if __name__ == '__main__':
    main() 
