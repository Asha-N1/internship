# functions in python
def my_function(): # defining function
    print("python programs")


# add 2 num
def add(a,b): # defining add function with 2 arguments
    c= a+b
    print(c)




def add_sub(a,b): # defining add function with 2 arguments
    c = a+b
    d = a-b
    return c,d




def main():
    
    a=10
    b=20
    my_function() # calling function
    add(a,b) # calling add function with 2 arguments values
 
    add_sub(a,b)
    result1,result2=add_sub(4,6) # using return we are calling function
    print(result1,result2)

if __name__ == '__main__':
    main()
