# This is the implementation of a perceptron in python
#
# Developed by:
# Alam Tellez
# Fermin Moreno

'''
2
4
3
1, 1, 0
0, 1, 1
1, 0, 1
0, 0, 0
-1, -1
2, 2
0, 0
'''

import random
import math

def activation_function(vals, weights, threshold):
    result = 0
    for i in range(len(vals)):
        #print(vals[i], weights[i])
        result += vals[i] * weights[i]
    #print(result)
    if result > threshold:
        return 1
    else:
        return 0

def update_weights(vals, weights, threshold):
    output = vals[1]
    a_function_result = activation_function(vals[:-1], weights, threshold)
    #print(a_function_result)
    error = output - a_function_result
    for i in range(len(weights)):
        weights[i] += error * vals[i]
    return (error, weights)

# The number of weights is defined by the dimensionality of the input
def starting_weights(weights, dimensionality):
    for i in range(dimensionality):
    	weights.append(random.randint(0,1))

def train_newtork(train_set, weights, epochs, threshold):
    for i in range(epochs):
        error = 0
        for j in range(len(train_set)):
            aux_error, weights = update_weights(train_set[j], weights, threshold)
            error += pow(aux_error, 2)
            # This is just to prevent overfitting
            if error == 0:
                break
    return (error, weights)

def test_network(test_set, error, weights, threshold):
    if error >= 1 or len(test_set) == 0:
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
    weights = []
    for _ in range(train_size):
        train_set.append(list(map(float,input().replace(" ", "").split(","))))
    for _ in range(test_size):
        test_set.append(list(map(float,input().replace(" ", "").split(","))))

    starting_weights(weights, dimensionality)
    print(weights)
    epochs = 100
    threshold = random.randrange(0,2)
    error = 0
    error, weights = train_newtork(train_set, weights, epochs, threshold)

    test_network(test_set, error, weights, threshold)
