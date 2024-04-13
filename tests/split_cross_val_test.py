import os
import sys

import pandas as pd
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.split_cross_val import split_cross_val


# Test whether the function returns a dictionary containing the results for logistic regression 
# and random forests models as pd.Series objects, each with the expected number of results.
def test_split_cross_val_results():
    results = split_cross_val(
        "data/processed/planet-systems.csv", "st_spectype", split=0.7, folds=5
    )

    assert (
        "logistic" in results
    ), "Result of logistic regression model should be returned"
    assert (
        "random_forest" in results
    ), "Result of random forests model should be returned"
    assert isinstance(
        results["logistic"], pd.Series
    ), "Item returned should be a pd.Series object"
    assert isinstance(
        results["random_forest"], pd.Series
    ), "Item returned should be a pd.Series object"
    assert (
        len(results["logistic"]) == len(results["random_forest"]) == 4
    ), "There should be 4 results returned"


# Checks that the function returns a dictionary of scores with the appropriate keys, 
# ensuring that fit time, score time, test score, and train score are present for each model.
def test_split_cross_val_scores():

    results = split_cross_val(
        "data/processed/planet-systems.csv", "st_spectype", split=0.7, folds=5
    )

    # Check if the scores are in the expected format
    for model, scores in results.items():
        assert "fit_time" in scores, f"Fit time should be in the {model} model scores."
        assert (
            "score_time" in scores
        ), f"Score time should be in the {model} model scores."
        assert (
            "test_score" in scores
        ), f"Test score should be in the {model} model scores."
        assert (
            "train_score" in scores
        ), f"Train score should be in the {model} model scores."


# Verifies that the function raises appropriate exceptions when provided 
# with invalid parameters. This includes testing for an invalid target column, 
# a non-existing file path, an invalid split ratio, and an invalid number of folds.
def test_invalid_parameters():

    # Invalid target column
    with pytest.raises(KeyError):
        split_cross_val(
            "data/processed/planet-systems.csv", "invalid_col", split=0.7, folds=5
        )

    # Non-existing data
    with pytest.raises(FileNotFoundError):
        split_cross_val(
            "data/processed/planet-systems-cleaned.csv",
            "st_spectype",
            split=0.7,
            folds=5,
        )

    # Invalid split ratio
    with pytest.raises(ValueError):
        split_cross_val(
            "data/processed/planet-systems.csv", "st_spectype", split=1.7, folds=5
        )

    # Non-existing data
    with pytest.raises(ValueError):
        split_cross_val(
            "data/processed/planet-systems.csv", "st_spectype", split=0.7, folds=-1
        )
