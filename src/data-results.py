# This script will assess two models against our dataset
# of the magnitudes of bands for each star

# Imports
import click
import pandas as pd
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Main function 
@click.command()
@click.argument('cleaned_input_data', type=str)
@click.argument('results_csv_folder', type=str)
@click.argument('confusion_matrix_png', type=str)


def main(cleaned_input_data, x_train_output, x_test_output, results_csv_folder, confusion_matrix_png):

    #access data from cleaned data file
    data = pd.read_csv(f'{cleaned_input_data}')

    #should we include the following as a table? !!!!!
    only_stars_data.describe(include="all")

    # Setting y to our predicted variable: st_spectype
    y = only_stars_data["st_spectype"]
    
    # Our predictors will be the following 5 features
    X = only_stars_data[["sy_umag", "sy_gmag", "sy_rmag", "sy_imag", "sy_zmag"]]

    # Creating a 75% train test split to run on our data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

    # Logistic Regression cross validation and saved to csv
    pipe = make_pipeline(StandardScaler(), LogisticRegression())
    lr_df = pd.DataFrame(cross_validate(pipe, X_train, y_train, return_train_score=True)).mean()
    lr_df.to_csv(f'{results_output_folder}/logistic_regression_df.csv')

    # RandomForest Classifier
    rfc = RandomForestClassifier(n_estimators=275, random_state=123)
    pipe2 = make_pipeline(StandardScaler(), rfc)
    
    # Calculate mean cross_val_score score of test scores
    cv_results = cross_val_score(pipe2, X, y, cv=5, scoring='accuracy')
    
    # RandomForest Classifier cross validation and saved to csv
    pipe2.fit(X_train, y_train)
    rfc_df = pd.DataFrame(cross_validate(pipe2, X_train, y_train, return_train_score=True)).mean()
    rfc_df.to_csv(f'{results_output_folder}/random_forest_classifier_df.csv')
    
    # Calculating the accuracy of our predictions made on the test set
    predictions = rfc.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    pd.DataFrame(accuracy).to_csv(f'{results_output_folder}/accuracy.csv', index = False)

    # Creating a validation set for our confusion matrix
    X_train_2, X_valid, y_train_2, y_valid = train_test_split(X_train, y_train, test_size=0.3, random_state=123)

    # Train the model on the training set
    pipe.fit(X_train, y_train)

    # Predict y values for the validation set
    predictions = pipe.predict(X_valid)
    
    # Compare the predicted y values with actual y values of the validaiton set using the confusion matrix
    cm = confusion_matrix(y_valid, predictions)
    pd.DataFrame(cm).to_csv(f'{results_output_folder}/confusion_matrix.csv', index = False)
    
    #Visualization of the confusion matrix using 'ConfusionMatrixDisplay'
    ConfusionMatrixDisplay.from_predictions(y_valid, predictions)
    plt.savefig(f'{confusion_matrix_png}/confusion_matrix.png')


if __name__ == '__main__':
    main() 

