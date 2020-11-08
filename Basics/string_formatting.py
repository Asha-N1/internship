# string formatting in python

def fun_1(): # function defination
    name = "asha"
    age = 24
    print("my name is {} my age is {}".format(name, age)) # formatting function
fun_1() # function call

def fun_2():  # function defination
    y = "is"
    x = "python programing language {} to understand" # another way of using format
    print(x.format(y))
fun_2()  # function call

def fun_3():  # function defination
    a = 10
    b = 20
    c = 30
    z = "add {0} and {1} and also {2}"
    print(z.format(a,b,c)) # passing multiple arguments
    print(z.format(a+2,b,c)) # we can perform operations also
fun_3()  # function call
