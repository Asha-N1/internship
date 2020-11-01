# numpy in arrays copy and view 

import numpy as np # importing numpy as np

def copy():
    arr = np.array([1,2,3,4,5]) # creating array 
    arr1 = arr.copy() # copying array to new variable
    arr[0] = 6 # adding element to the existing array
    print(arr) #  after adding the element
    print(arr1) # disply the array before we adding element copying the same array
    arr2 = arr.view() # disply the array after affecting of original array
    print(arr) # modified array
    print(arr2) # modified array

    x = arr.copy() # copying array
    y = arr.view() # view array

    print(x.base) # displaying base of copying of array
    print(y.base)  # displaying base of view of array

copy() # calling function


