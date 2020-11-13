# Array usage in python
from array import *

def fun_arrays(vals): # creating function 
    vals.reverse() # reverse an array
    vals.remove(1) # remove element from array
    vals.append(7) # adding 7 element to array
    for i in range(5): # using for loop printing array one by one
        print(i)

# main function
def main():
    vals = array('i',[1,2,9,5,4,6]) # creating array
    print(vals)                     # print array
    print(vals.buffer_info()) # display the address of array and size of array
    print(vals.typecode) # it display the type of the array
    fun_arrays(vals)     # calling function
    print(vals) # display array in reverse
    print(vals) # display array removed element
    print(vals) # display appened element to array
    print(vals[0]) # displaying 0 position element in array
    

# main excecution
if __name__ == '__main__':
    main()

