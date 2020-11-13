# Exception in python

def exce(num1,num2): # function for exception
    try: # try block
        print(num1/num2)
    except Exception as e: # handling exception
        print("hey, you cant divided num by zero",e)

    finally:

        print("i wont consider try block and exception") # finally block

 
def main():
    num1 = 10
    num2 = 0
    exce(num1,num2) # calling function

if __name__ == '__main__':
    main()





