import pytest
import pandas as pd


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
# Test 2: Makes sure csv matches the expected test data given
# Test 3: Ensures boxplot is saved to the given directory
# Test 4: Ensures boxplot matches the expected test data given
# Test 5: Makes sure an error is thrown if boxplot is not generated
# Test 6: Makes sure an error is thrown if csv is not generated