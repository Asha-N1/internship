# functions in python
def my_function(): # defining function
    print("python programs")

# add 2 num
def add(num1,num2): # defining add function with 2 arguments
    addition= num1+num2
    print(addition)

# add-sub function
def add_sub(num1,num2): # defining add function with 2 arguments
    addition = num1+num2
    subtraction = num1-num2
    return addition, subtraction

# main function
def main():
    num1=10
    num2=20
    my_function() # calling function
    add(num1,num2) # calling add function with 2 arguments values
    add_sub(num1,num2)
    result1,result2=add_sub(4,6) # using return we are calling function
    print(result1,result2)

if __name__ == '__main__':
    main()
