# numpy array shapes and reshapes

import numpy as np

def array_shapes(): # function for shape of array
    arr = np.array([[1,2,3,5,7,6],[2,7,4,8,9,0]]) # passing 2-d array
    print(arr.shape) # calling array with shape
array_shapes() # calling function

def array_shapes1(): # defining function
    arr = np.array([1,2,3,4,5,6], ndmin=6) # creating array with 6-d
    print(arr) # printing array
    print("shape of array", arr.shape) # shape of array
array_shapes1() # calling the function



def array_reshape(): # function for reshape
    arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # passing elements to array
    newarr = arr2.reshape(4, 3) # reshape array with 4 cols and rows
    print(newarr)  # print newarry
array_reshape() # function call
        