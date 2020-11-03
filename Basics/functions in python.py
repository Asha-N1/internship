# functions in python
def my_function(): # defining function
    print("python programs")
my_function() # calling function

# add 2 num
def add(a,b): # defining add function with 2 arguments
    c= a+b
    print(c)
add(4,6) # calling add function with 2 arguments values



def add_sub(a,b): # defining add function with 2 arguments
    c = a+b
    d = a-b
    return c,d

result1,result2=add_sub(4,6) # using return we are calling function
print(result1,result2)
