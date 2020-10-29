
import numpy as np #importing numpy

def array_index(): # creating function 
    arr = np.array([1, 2, 3, 4]) # acessing numpy module
    print(arr[3]) # specifying array index
    print(arr[0] + arr[3]) # adding index position values
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]]) # 2-d array
    print('2nd element on 1st dim: ', arr[0, 1]) # display 2nd element of 1st d-array
    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # 3-d array
    print(arr[0, 1, 2]) # Access the third element of the second array of the first array
array_index() # calling function