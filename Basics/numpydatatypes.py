# data types in numpy

import numpy as np # importing numpy 

def data_types(): # function for datatypes
    arr = np.array([7,5,8,2]) # intializing array elements
    print(arr.dtype) # type of given array
    arr1 = np.array([1, 2, 3, 4], dtype='S') # array with string data type
    print(arr1.dtype) 
    arr2 = np.array([1, 0, 3]) # defining array
    newarr = arr2.astype(bool) # converting to bool
    print(newarr) # displying bool type array
    print(newarr.dtype) 
data_types() # calling function


