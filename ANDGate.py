#####################################################################################################################
#####################################################################################################################


#####################################################################################################################
#####################################################################################################################
def activationFunction(n):

    #TODO - Application 1 - Step 4b - Define the binary step function as activation function





    return
#####################################################################################################################
#####################################################################################################################


#####################################################################################################################
#####################################################################################################################
def forwardPropagation(p, weights, bias):

    a = None # the neuron output

    # TODO - Application 1 - Step 4a - Multiply weights with the input vector (p) and add the bias   =>  n



    # TODO - Application 1 - Step 4c - Pass the result to the activation function  =>  a



    return a
#####################################################################################################################
#####################################################################################################################


#####################################################################################################################
#####################################################################################################################
def main():

    #Application 1 - Train a single neuron perceptron in order to predict the output of an AND gate.
    #The network should receive as input two values (0 or 1) and should predict the target output


    #Input data
    P = [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]

    #Labels
    t = [0, 0, 0, 1]

    #TODO - Application 1 - Step 2 - Initialize the weights with zero  (weights)


    #TODO - Application 1 - Step 2 - Initialize the bias with zero  (bias)


    #TODO - Application 1 - Step 3 - Set the number of training steps  (epochs)
    epochs = 100

    #TODO - Application 1 - Step 4 - Perform the neuron training for multiple epochs
    for ep in range(epochs):
        for i in range(len(t)):

            #TODO - Application 1 - Step 4 - Call the forwardPropagation method


            #TODO - Application 1 - Step 5 - Compute the prediction error (error)


            #TODO - Application 1 - Step 6 - Update the weights


            #TODO - Application 1 - Step 7 - Update the bias

            # DELETE THIS
            continue

    #TODO - Application 1 - Step 8 - Print weights and bias

   
    # TODO - Application 1 - Step 9 - Display the results

   
    return
#####################################################################################################################
#####################################################################################################################



#####################################################################################################################
#####################################################################################################################
if __name__ == "__main__":
    main()
#####################################################################################################################
#####################################################################################################################