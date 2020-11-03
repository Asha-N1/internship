# Array usage in python
from array import *

vals = array('i',[1,2,9,5,4,6]) # creating array
print(vals)

print(vals.buffer_info()) # display the address of array and size of array
print(vals.typecode) # it display the type of the array
vals.reverse() # display array in reverse
print(vals)
vals.remove(1) # remove the element 1 from array
print(vals)
vals.append(7) # adding 7 element to array
print(vals)

print(vals[0])

for i in range(5): # using for loop printing array one by one
    print(i)



