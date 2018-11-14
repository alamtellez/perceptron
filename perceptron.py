# This is the implementation of a perceptron in python
#
# Developed by:
# Alam Tellez
# Fermin Moreno

import random
import math

def activation_function(vals, weights, threshold):
    result = 0
    for i in range(len(vals)):
        result += vals[i] * weights[i]
    if result > threshold:
        return 1
    else:
        return 0

def update_weights(vals, weights, threshold):
    output = vals[-1]
    a_function_result = activation_function(vals[0:-1], weights, threshold)
    error = output - a_function_result
    for i in range(len(weights)):
        weights[i] += error * vals[i]
    return (error, weights)

# The number of weights is defined by the dimensionality of the input
def starting_weights(weights, dimensionality):
    for i in range(dimensionality):
        # Setting small random numbers to the initial weights
        weights.append(random.randrange(0, 1))
    return weights

def train_newtork(train_set, weights, epochs, threshold):
    for i in range(epochs):
        error = 0
        for vals in train_set:
            aux_error, weights = update_weights(vals, weights, threshold)
            error += pow(aux_error, 2)
            # This is just to prevent overfitting
            if error == 0:
                break
    return (error, weights)

def test_network(test_set, error, weights, threshold):
    if error >= 1:
        print("no solution found")
    else:
        for vals in test_set:
            print(activation_function(vals, weights, threshold))

if __name__ == "__main__":

    dimensionality = int(input())
    train_size = int(input())
    test_size = int(input())
    train_set = []
    test_set = []
    for i in range(train_size):
        train_set.append(list(map(int,input().replace(" ", "").split(","))))
    for i in range(test_size):
        test_set.append(list(map(int,input().replace(" ", "").split(","))))
    # train_set = list(map(int, train_set))
    # test_set = list(map(int, test_set))


    weights = starting_weights([], dimensionality)
    epochs = 100
    threshold = random.randrange(1, 10)
    error = 0
    error, weights = train_newtork(train_set, weights, epochs, threshold)

    test_network(test_set, error, weights, threshold)
