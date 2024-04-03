import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
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

@pytest.fixture(scope="session", autouse=True)
def create_test_directories():
    test_csv_dir = "results/tables"
    test_bp_dir = "results/figures"

    # Create directories if they don't exist
    os.makedirs(test_csv_dir, exist_ok=True)
    os.makedirs(test_bp_dir, exist_ok=True)

    yield test_csv_dir, test_bp_dir


# Test 1: Ensures csv is saved to the given directory
def test_csv_saves_to_dir(test_data, create_test_directories): #this is what chatgpt wants but this also doesnt work
    test_csv_dir, test_bp_dir = create_test_directories
    column_star = "column_star"

    make_boxplot_and_table(test_data, column_star, test_csv_dir, test_bp_dir)
    assert os.path.exists(f"{test_csv_dir}/{column_star}.csv"), "Csv file was not saved properly!"

# Test 2: Makes sure csv matches the expected test data given

def test_csv_matches(test_data, test_csv_dir, test_bp_dir):
    column_moon = "column_moon"
    make_boxplot_and_table(test_data, column_moon, test_csv_dir, test_bp_dir)
    dir_csv_data = pd.read_csv(f"{test_csv_dir}/{column_moon}.csv")
    test_csv_data = test_data[["st_spectype", column_moon]].groupby("st_spectype").describe()
    assert dir_csv_data.equals(test_csv_data), "Csv files do not match eachother!"
    
# Test 3: Ensures boxplot is saved to the given directory

def test_bp_saves_to_dir(test_data,test_csv_dir, test_bp_dir):
    column_sun = "column_sun"
    make_boxplot_and_table(test_data, column_sun, test_csv_dir, test_bp_dir)
    assert os.path.exists(f"{test_bp_dir}/{column_sun}.png"), "Boxplot file was not saved properly"

# Test 4: Ensures boxplot matches the expected test data given

def test_bp_matches(test_data, test_csv_dir, test_bp_dir):
    column_moon = "column_moon"
    make_boxplot_and_table(test_data, column_moon, test_csv_dir, test_bp_dir)
    dir_bp_read = plt.imread(f"{test_bp_dir}/{column_moon}.png")
    test_bp_data = test_data[["st_spectype", {column_moon}]].groupby("st_spectype").describe().boxplot()
    test_bp_fig = test_bp_data.figure.savefig("function_boxplot.png")
    test_bp_read = plt.imread
    assert dir_bp_read == test_bp_read, "Boxplot figures do not match eachother!"

# Test 5: Checks if an invalid path is given

def test_invalid_path(test_data):
    column_moon = "column_moon"
    with pytest.raises(RuntimeError) as e:
        make_boxplot_and_table(test_data, column_moon, "/path/doesntwork", "/path/doesntwork")
    assert str(e.value) == "Error occurred: [Errno 2] No such file or directory: '/invalid/path'"
    

    

 


