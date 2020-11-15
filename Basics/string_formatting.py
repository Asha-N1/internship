# string formatting in python


def fun_1(name,age): # function defination
    print("my name is {} my age is {}".format(name, age)) # formatting function

def fun_2():  # function defination
    y = "is"
    x = "python programing language {} to understand" # another way of using format
    print(x.format(y))


def fun_3(num1,num2,num3):  # function defination
    z = "add {0} and {1} and also {2}"
    print(z.format(num1,num2,num3)) # passing multiple arguments
    print(z.format(num1+2,num2,num3)) # we can perform operations also

# main function
def main():
    name = "asha"
    age = 24
    num1 = 10
    num2 = 20
    num3 = 30
    fun_1(name,age) # function call
    fun_2()  # function call
    fun_3(num1,num2,num3)  # function call


# main execution
if __name__ == '__main__':
    main()