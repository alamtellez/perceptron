# This is the implementation of a perceptron in python
#
# Developed by:
# Alam Tellez
# Fermin Moreno

if __name__ == "__main__":
    
    dimensionality = int(input())
    train_size = int(input())
    test_size = int(input())
    train_set = []
    test_set = []
    for _ in range(train_size):
        train_set.append(list(map(int,input().replace(" ", "").split(","))))
    for _ in range(test_size):
        test_set.append(list(map(int,input().replace(" ", "").split(","))))
    # train_set = list(map(int, train_set))
    # test_set = list(map(int, test_set))
    
    print(train_set, test_set)