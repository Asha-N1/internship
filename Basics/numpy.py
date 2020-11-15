import numpy  # importing numpy module

arr = numpy.array([1,2,3,4,5])  # calling numpy
print(arr)
print(type(arr))  # showing array type

# we can improve numpy as  alias
import numpy as np

arr= np.array([1,2,3,4,5])
print(arr)

print(np.__version__) # display the version of numpy

a = np.array(20)
print(a) # zero dimension array or scalar
print(a.ndim)
a = np.array([9,8,7,6,5]) # 1-D array
print(a)
print(a.ndim)
a = np.array([[2,6,8],[3,9,1]]) # 2-D array
print(a)
print(a.ndim)
a = np.array([[[1,2,3],[2,1,3]],[[9,8,7],[3,4,5]]]) # 3-D array
print(a)
print(a.ndim) # used to check dimensions of array
