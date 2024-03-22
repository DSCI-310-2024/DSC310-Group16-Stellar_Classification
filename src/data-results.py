# This script will assess two models against our dataset
# of the magnitudes of bands for each star

# Imports
import os

import click
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (ConfusionMatrixDisplay, accuracy_score,
                             confusion_matrix)
from sklearn.model_selection import (cross_val_score, cross_validate,
                                     train_test_split)
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler
from traitlets import default


# Main function
@click.command()
@click.option(
    "--cleaned_input_data", type=str, default="data/processed/planet-systems.csv"
)
@click.option("--results_csv_dir", type=str, default="results/tables")
@click.option("--conf_matrix_png_dir", type=str, default="results/figures")
def main(cleaned_input_data, results_csv_dir, conf_matrix_png_dir):
    print("### Running data-results.py ###")
    # create folders if they don't exist
    [os.makedirs(dir, exist_ok=True) for dir in [results_csv_dir, conf_matrix_png_dir]]

    # access data from cleaned data file
    only_stars_data = pd.read_csv(f"{cleaned_input_data}")

    # Create and save this as a table
    describe = only_stars_data.describe(include="all")
    pd.DataFrame(describe).to_csv(f"{results_csv_dir}/description_df.csv", index=False)

    # Setting y to our predicted variable: st_spectype
    y = only_stars_data["st_spectype"]

    # Our predictors will be the following 5 features
    X = only_stars_data[["sy_umag", "sy_gmag", "sy_rmag", "sy_imag", "sy_zmag"]]

    # Creating a 75% train test split to run on our data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=123
    )

    # Created and saved a y value count df
    pd.DataFrame(y_train.value_counts(normalize=True)).to_csv(f"{results_csv_dir}/y-values_df.csv", index=False)

    # Logistic Regression cross validation and saved to csv
    pipe = make_pipeline(StandardScaler(), LogisticRegression())
    lr_df = pd.DataFrame(
        cross_validate(pipe, X_train, y_train, return_train_score=True)
    ).mean()
    lr_df.to_csv(f"{results_csv_dir}/logistic_regression_df.csv")

    # RandomForest Classifier
    rfc = RandomForestClassifier(n_estimators=275, random_state=123)
    pipe2 = make_pipeline(StandardScaler(), rfc)

    # Calculate mean cross_val_score score of test scores
    cv_results = cross_val_score(pipe2, X, y, cv=5, scoring="accuracy")

    # RandomForest Classifier cross validation and saved to csv
    pipe2.fit(X_train, y_train)
    rfc_df = pd.DataFrame(
        cross_validate(pipe2, X_train, y_train, return_train_score=True)
    ).mean()
    rfc_df.to_csv(f"{results_csv_dir}/random_forest_classifier_df.csv")

    # Calculating the accuracy of our predictions made on the test set
    predictions = rfc.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    pd.DataFrame([accuracy], columns=["rf_accuracy"]).to_csv(
        f"{results_csv_dir}/accuracy.csv", index=False
    )

    # Creating a validation set for our confusion matrix
    X_train_2, X_valid, y_train_2, y_valid = train_test_split(
        X_train, y_train, test_size=0.3, random_state=123
    )

    # Train the model on the training set
    pipe.fit(X_train, y_train)

    # Predict y values for the validation set
    predictions = pipe.predict(X_valid)

    # Compare the predicted y values with actual y values of the validaiton set using the confusion matrix
    cm = confusion_matrix(y_valid, predictions)
    pd.DataFrame(cm).to_csv(f"{results_csv_dir}/confusion_matrix.csv", index=False)

    # Visualization of the confusion matrix using 'ConfusionMatrixDisplay'
    ConfusionMatrixDisplay.from_predictions(y_valid, predictions)
    plt.savefig(f"{conf_matrix_png_dir}/confusion_matrix.png")

    print("### Successfully ran data-results.py ###")


if __name__ == "__main__":
    main()
