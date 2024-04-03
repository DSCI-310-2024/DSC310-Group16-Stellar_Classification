import pandas as pd
import pytest
import sys
import os

# Import the clean_confidence_intervals function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.clean_confidence_intervals import clean_confidence_intervals

# Test that the function correctly processes columns containing
# the confidence interval and keeps only the mean value
def test_clean_confidence_intervals_removes_intervals(example_data_frame):
    cleaned_df = clean_confidence_intervals(example_data_frame)
    # Expected values after cleaning, assuming the function extracts the mean value correctly
    expected_umag = ['13.0932000', '15.1234000', '17.5678000']
    # Testing one column as representative; similar tests can be done for other columns
    assert cleaned_df['sy_umag'].tolist() == expected_umag, "Failed to remove intervals from sy_umag."

# Test that non-string columns remain unchanged
def test_clean_confidence_intervals_non_string_columns_unchanged(example_data_frame):
    # Adding purely numeric columns for this test
    example_data_frame['numeric_column'] = [100, 200, 300]
    cleaned_df = clean_confidence_intervals(example_data_frame)
    assert cleaned_df['numeric_column'].equals(example_data_frame['numeric_column']), "Numeric columns should not be altered."

# Test that columns not following the confidence interval format remain unaffected
def test_clean_confidence_intervals_does_not_affect_other_columns(example_data_frame):
    cleaned_df = clean_confidence_intervals(example_data_frame)
    # Assuming st_spectype should remain unchanged
    assert cleaned_df['st_spectype'].equals(example_data_frame['st_spectype']), "st_spectype was unexpectedly altered."

# Test that the function handles missing values correctly without errors
def test_clean_confidence_intervals_handles_missing_values(example_data_frame):
    example_data_frame.at[1, 'sy_umag'] = np.nan  # Introduce a NaN value
    cleaned_df = clean_confidence_intervals(example_data_frame)
    assert cleaned_df['sy_umag'].isnull().sum() == 1, "Failed to correctly handle NaN values in sy_umag."

# Test that the function can process columns that are entirely NaN.
def test_clean_confidence_intervals_all_nan_columns(example_data_frame):
    example_data_frame['all_nan'] = [np.nan, np.nan, np.nan]
    cleaned_df = clean_confidence_intervals(example_data_frame)
    assert cleaned_df['all_nan'].isnull().all(), "Columns with all NaN values should remain unchanged."

# Test handling empty strings and strings with non-standard separators.
def test_clean_confidence_intervals_empty_strings_and_non_standard_separators(example_data_frame):
    example_data_frame['sy_gmag'] = [
        '',  # empty string
        '20.0000-otherseparator0.0020',  # non-standard separator
        '21.0000',  # plain number
        '22.0000&plusmn;0.0020'  # correct format
    ]
    cleaned_df = clean_confidence_intervals(example_data_frame)
    expected_gmag = ['', '20.0000-otherseparator0.0020', '21.0000', '22.0000']
    assert cleaned_df['sy_gmag'].tolist() == expected_gmag, "Failed to handle empty strings and non-standard separators correctly."

# Test handling mixed formats within columns that should follow the confidence interval format.
def test_clean_confidence_intervals_mixed_formats(example_data_frame):
    example_data_frame['sy_umag'] = [
        '13.0932000&plusmn;0.0039422',  # correct format
        '15.0000',  # plain number
        np.nan,  # missing value
        'invalid format',  # not following expected format
        '17.5678000±0.0009876'  # different separator but valid format
    ]
    cleaned_df = clean_confidence_intervals(example_data_frame)
    expected_umag = ['13.0932000', '15.0000', np.nan, 'invalid format', '17.5678000']
    assert cleaned_df['sy_umag'].tolist() == expected_umag, "Failed to correctly handle mixed formats in sy_umag."