import os
import sys
from pathlib import Path

import pandas as pd
import pytest
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.read_data import fetch_data


@pytest.fixture
def url():
    base_url = "https://exoplanetarchive.ipac.caltech.edu"
    columns = "pl_name,st_spectype"
    return f"{base_url}/TAP/sync?query=select+{columns}+from+ps&format=csv"


@pytest.fixture
def output_path():
    return "data/raw/test_data.csv"


def test_fetch_data_downloads_data(url, output_path):
    df = fetch_data(url, output_path)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert os.path.exists(output_path)


def test_fetch_data_raises_exception_for_invalid_url(url, output_path):
    url = "invalid_url"
    with pytest.raises(requests.exceptions.RequestException):
        fetch_data(url, output_path)


def test_fetch_data_saves_data_to_specified_output_path(url, output_path):
    output_path = "data/raw/custom_test_data.csv"
    fetch_data(url, output_path)
    assert os.path.exists(output_path)


def test_fetch_data_default_output_path(url, output_path):
    fetch_data(url, None)
    default_output_path = Path("data/raw/planet-systems.csv")
    assert os.path.exists(default_output_path)


def test_fetch_data_response_is_dataframe(url, output_path):
    df = fetch_data(url, output_path)
    assert isinstance(df, pd.DataFrame)


def test_fetch_data_downloads_data_from_default_url(url, output_path):
    fetch_data(None, output_path)
    assert os.path.exists(output_path)
