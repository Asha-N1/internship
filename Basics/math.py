# math function in python
import math # importing math module

def squr_fun(): # squr function
    square= math.sqrt(25) # using math performing square root of 25
    print(square)


def floor_fun(): #floor function
    val = 9.56
    print(math.floor(val)) # floor will give least value
    print(math.ceil(val)) # ceil will give high value


def pow_fun():  # power function
    print(math.pow(2,3)) # power function
    print(math.pi) # pi value
    print(math.e)
 
def positive():  # positive function
    val1=-980.787
    print(abs(val1)) # positive value

def max_fun():
    val2 = max(12,3,5) # max build in math function
    print(val2)

def min_fun():
    val3 = min(12,3,5) # min build in math function
    print(val3)

# main function
def main():
    squr_fun() # calling function
    floor_fun() # calling function
    pow_fun()
    positive()   
    max_fun()
    min_fun()
  
    
# main execution
if __name__ == '__main__':
    main()



