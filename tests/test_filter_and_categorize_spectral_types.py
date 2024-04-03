import pandas as pd
import pytest
import sys
import os

# Import the filter_and_categorize_spectral_types function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.clean_preprocess_data import filter_and_categorize_spectral_types