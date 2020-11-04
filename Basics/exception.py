# Exception in python

def exce(): # function for exception
    a = 10
    b = 0
    try: # try block
        print(a/b)
    except Exception as e: # handling exception
        print("hey, you cant divided num by zero",e)

    finally:

        print("i wont consider try block and exception") # finally block
exce() # calling function
 





