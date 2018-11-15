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

def update_weights(train_vals, weights, treshold):
	last = train_vals[-1]
	a_function_result  = activation_function(train_vals[:-1], weights, treshold)
	#print(a_function_result)
	error = last - a_function_result
	for i in range(len(weights)):
		weights[i] += error * train_vals[i]
	return error

def start_weights(weights, dimensionality):
    # Setting small random numbers to the initial weights
    for i in range(dimensionality):
    	weights.append(0)
    
def train_newtork(epochs, train_set, threshold, weights):
    for _ in range(epochs):
        error = 0
        for val in train_set:
    
            aux_error = update_weights(val, weights, threshold)
            error += pow(aux_error, 2)
        # This is just to prevent overfitting
        if error == 0:
            break
        
    #print(error)
    #print(weights)
    return error

def test_network(test_set, error, weights, threshold):
    if error >= 1 or len(test_set) == 0:
        print("no solution found")
    else:
        for vals in test_set:
            print(activation_function(vals, weights, threshold))
        
if __name__ == "__main__":
import matplotlib.pyplot as plt

    dimensionality = int(input())
    train_size = int(input())
    test_size = int(input())
    train_set = []
    test_set = []
    weights = [] 
    for _ in range(train_size):
        train_set.append(list(map(float,input().rstrip('\n').rstrip('\r').replace(" ", "").split(","))))
    for _ in range(test_size):
        test_set.append(list(map(float,input().rstrip('\n').rstrip('\r').replace(" ", "").split(","))))
    
    
    plt.scatter(weight1,height1,c='b',marker='o')
    plt.xlabel('weight', fontsize=16)
    plt.ylabel('height', fontsize=16)
    plt.title('scatter plot - height vs weight',fontsize=20)
    plt.show()