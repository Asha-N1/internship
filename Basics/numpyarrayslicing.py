# array silcing in numpy

import numpy  # importing numpy library

def array_slicing(): # defining function array_slicing
    arr = numpy.array(['asha','deeksha','vani','rani','ganu']) # providing elements to array and calling numpy
    print(arr[2:4]) # array slicing in numpy
    print(arr[1:]) # specifying only starting index
    print(arr[:3]) # specifying ending index only
    print(arr[::]) # not providing any index
    print(arr[-0:-3]) # negative indexing
    print(arr[1:3:5]) # step of slicing
array_slicing() # calling function

# 2-D array slicing

def array_slice__2d(): # defining function array_slice_2d
    arr1 = numpy.array([['asha','deeksha','vani','rani','ganu'],['anil','varun','sree','ram','ayan']]) # 2-d array
    print(arr1[0:2, 4 ]) # both element returns index 4
    print(arr1[0:2, 1:4 ])  # it will display between 0 to 4 elements in 2-D array
array_slice__2d() # calling 2-d array function
