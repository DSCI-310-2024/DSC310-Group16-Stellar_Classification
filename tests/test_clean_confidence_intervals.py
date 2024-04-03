import pytest
import pandas as pd
from src.clean_preprocess_data import clean_confidence_intervals

def test_clean_confidence_intervals():
    test_data = pd.DataFrame({
        'col1': ['10.5&0.3', '9.8&0.2'],
        'col2': ['A&B', 'C&D']
    })
    expected_result = pd.DataFrame({
        'col1': ['10.5', '9.8'],
        'col2': ['A', 'C']
    })
    result = clean_confidence_intervals(test_data)
    pd.testing.assert_frame_equal(result, expected_result)
