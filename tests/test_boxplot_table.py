import pytest
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.boxplot_table_function import make_boxplot_and_table


@pytest.fixture
# Create a test Dataframe with our requires st_spectype column and our other columns
def test_data():
    data = {
        "st_spectype": ["A", "A", "B", "C", "A","C"],
        "column_star": [2, 5, 6, 8, 1, 3],
        "column_moon": [4, 9, 10, 22, 5, 14],
        "column_sun": [13, 5, 2, 3, 12, 10],
        "column_pluto": [4, 7, 1, 10, 8, 9]
    }
    return pd.DataFrame(data)

test_csv_dir = "results/tables"
test_bp_dir = "results/figures"


# Test 1: Ensures csv is saved to the given directory
column_star = "column_star"

def test_csv_saves_to_dir(test_data):
    make_boxplot_and_table(test_data, column_star, test_csv_dir, test_bp_dir)
    assert os.path.exists(f"{test_csv_dir}/{column_star}.csv"), "Csv file was not saved properly!"

# Test 2: Makes sure csv matches the expected test data given
column_moon = "moon"

def test_csv_matches(test_data):
    make_boxplot_and_table(test_data, column_moon, test_csv_dir, test_bp_dir)
    dir_csv_data = pd.read_csv(f"{test_csv_dir}/{column_moon}.csv")
    test_csv_data = test_data[["st_spectype", {column_moon}]].groupby("st_spectype").describe()
    assert dir_csv_data.equals(test_csv_data), "Csv files do not match eachother!"
    
    
# Test 3: Ensures boxplot is saved to the given directory
column_sun = "column_sun"

def test_bp_saves_to_dir(test_data):
    make_boxplot_and_table(test_data, column_sun, test_csv_dir, test_bp_dir)
    assert os.path.exists(f"{test_bp_dir}/{column_star}.png"), "Boxplot file was not saved properly"

# Test 4: Ensures boxplot matches the expected test data given
column_moon = "moon"

def test_csv_matches(test_data):
    make_boxplot_and_table(test_data, column_moon, test_csv_dir, test_bp_dir)
    dir_bp_png = plt.imread(f"{test_bp_dir}/{column_moon}.png")
    dir_bp_data = dir_bp_png.plot().get_figure()
    test_bp_data = test_data[["st_spectype", {column_moon}]].groupby("st_spectype").describe().boxplot()
    assert dir_bp_data.equals(test_bp_data), "Boxplot figures do not match eachother!"

# Test 7: Checks if an invalid path is given