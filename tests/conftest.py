import pytest
import pandas as pd

@pytest.fixture
def example_data_frame():
    """Provides a DataFrame for tests."""
    return pd.DataFrame({
        'temperature_str': ['300&10', '400&15', '500&20'],
        'st_spectype': ['G', 'K', None, 'M'],
        'sy_umag': [10.5, None, 9.8, 10.2],
        'sy_gmag': [10.1, 10.3, 10.2, 9.9],
        'sy_rmag': [9.9, 9.8, None, 9.7],
        'sy_imag': [9.7, 9.6, 9.5, 9.4],
        'sy_zmag': [9.5, 9.4, 9.3, 9.2]
    })
