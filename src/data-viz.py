# This script will create a PNG for the confusion matrix given the information gathered 
# from our analysis 

 # Imports 
import click
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

 # Main function 
 @click.command()
 @click.argument('X_train_data', type=str)
 @click.argument('Y_train_data', type=str)
 @click.argument('confusion_matrix', type=str)
 @click.argument('eda_png', type=str)



 def main():

     #create a second test split
     X_train_2, X_valid, y_train_2, y_valid = train_test_split(
        X_train_data, Y_train_data, test_size=0.3, random_state=123 
     )

     # Predict y values for the validation set
     predictions = pipeline_function.predict(X_valid)

     # create confusion matrix
     cm = confusion_matrix(y_valid, predictions)
     print(cm)

     #Display confusion matrix as a visualization
     ConfusionMatrixDisplay.from_predictions(y_valid, predictions)
     plt.show()

     plt.savefig(f'{viz_png}/confusion_matrix.png')

if __name__ == '__main__':
     main()





