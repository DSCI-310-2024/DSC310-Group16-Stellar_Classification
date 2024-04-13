# Imports
import os
import sys

import click
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.boxplot_table_function import make_boxplot_and_table


# Main function
@click.command()
@click.option(
    "--cleaned_input_data", type=str, default="data/processed/planet-systems.csv"
)
@click.option("--eda_png_dir", type=str, default="results/figures")
@click.option("--eda_csv_dir", type=str, default="results/figures")
@click.option("--box_plot_dir", type=str, default="results/figures")


def main(cleaned_input_data, eda_png_dir, eda_csv_dir, box_plot_dir):
    """
    Processes cleaned star data to generate visual and statistical analyses. 
    It reads a dataset from a specified path, produces a histogram of stellar 
    classifications, and creates detailed box plots and summary tables for 
    various magnitude measurements across specified bands. 
    The generated figures and tables are saved to designated directories for 
    further exploration and analysis.
    """
    # create dirs if they don't exist
    [
        os.makedirs(dir, exist_ok=True)
        for dir in [eda_png_dir, eda_csv_dir, box_plot_dir]
    ]

    # read data from cleaned data file
    data = pd.read_csv(f"{cleaned_input_data}")

    # store the value counts as a DataFrame
    types_summ = pd.DataFrame(data["st_spectype"].value_counts())

    # create and save the histogram
    fig, ax = plt.subplots(1, 1)
    types_summ.plot.bar(
        xlabel="Stellar classification", title="Counts of type of stars", ax=ax
    )

    for col in types_summ.columns:
        for id, val in enumerate(types_summ[col]):
            ax.text(id, val, str(val))

    plt.savefig(f"{eda_png_dir}/star_count_hist.png")

    # create and save the table and boxplot and boxplot for sy_umag
    make_boxplot_and_table(
        data=data, column_name="sy_umag", csv_dir=eda_csv_dir, box_plot_dir=box_plot_dir
    )

    # create and save the table and boxplot and boxplot for sy_gmag
    make_boxplot_and_table(
        data=data, column_name="sy_gmag", csv_dir=eda_csv_dir, box_plot_dir=box_plot_dir
    )

    # create and save the table and boxplot for sy_rmag
    make_boxplot_and_table(
        data=data, column_name="sy_rmag", csv_dir=eda_csv_dir, box_plot_dir=box_plot_dir
    )

    # create and save the table and boxplot for sy_imag
    make_boxplot_and_table(
        data=data, column_name="sy_imag", csv_dir=eda_csv_dir, box_plot_dir=box_plot_dir
    )

    # create and save the table and boxplot for sy_zmag
    make_boxplot_and_table(
        data=data, column_name="sy_zmag", csv_dir=eda_csv_dir, box_plot_dir=box_plot_dir
    )


if __name__ == "__main__":
    main()
