import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
from sklearn.metrics import accuracy_score
#####################################################################################################################
#####################################################################################################################



#####################################################################################################################
#####################################################################################################################
# TODO - Application 3 - Step 5 - Create the ANN model
def modelDefinition():

    # TODO - Application 3 - Step 5a - Define the model as a Sequential model
    model = None  # Modify this

    # TODO - Application 3 - Step 5b - Add a Dense layer with 8 neurons to the model


    # TODO - Application 3 - Step 5c - Add a Dense layer (output layer) with 1 neuron


    # TODO - Application 3 - Step 5d - Compile the model by choosing the optimizer(adam) ant the loss function (MSE)

    return model
#####################################################################################################################
#####################################################################################################################



#####################################################################################################################
#####################################################################################################################
def main():

    # TODO - Application 3 - Step 1 - Read data from "Houses.csv" file


    # TODO - Application 3 - Step 2 - Shuffle the data



    # TODO - Application 3 - Step 3 - Separate the data from the labels (x_data / y_data)
    #x_data = ...
    #y_data = ...


    # TODO - Application 3 - Step 4 - Separate the data into training/testing dataset
    #x_train = ...
    #y_train = ...

    #x_test = ...
    #y_test = ...


    # TODO - Application 3 - Step 5 - Call the function "modelDefinition"

    # TODO - Application 3 - Step 6 - Train the model for 100 epochs and a batch of 16 samples


    # TODO - Application 3 - Step 7 - Predict the house price for all the samples in the testing dataset


    # TODO - Exercise 8 - Compute the MSE for the test data
    mse = 0
    print("Mean Square Error = {}".format(mse))


    return
#####################################################################################################################
#####################################################################################################################



#####################################################################################################################
#####################################################################################################################
if __name__ == '__main__':
    main()
#####################################################################################################################
#####################################################################################################################