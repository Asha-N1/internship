# user input in python

def user_input(): # userinput  function
    val1 = int(input("enter 1st num:")) # user giving input
    val2= int(input("enter 2st num:"))
    res = val1 + val2
    print(res)
user_input() # calling function

def expr_fun(): # function for expression
    expr = eval(input("enter the expression:")) # we are using eval and providing expression as input
    print(expr)
expr_fun() # calling function