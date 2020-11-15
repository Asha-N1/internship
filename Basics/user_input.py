# user input in python

def user_input(val1,val2): # userinput  function
    res = val1 + val2
    print(res)

def expr_fun(expr): # function for expression
    print(expr)

# main function
def main():
    val1 = int(input("enter 1st num:")) # user giving input
    val2= int(input("enter 2st num:"))
    user_input(val1,val2) # calling function
    expr = eval(input("enter the expression:")) # we are using eval and providing expression as input
    expr_fun(expr) # calling function


# main execution
if __name__ == '__main__':
    main()
