# stacks in python


def stack_s(myStack = []): # defining function
     # creating empty stack
    myStack.append('a') # inserting elements into stack
    myStack.append('b')
    myStack.append('c')
    print(myStack)
    myStack.pop() # deleting elements from stack
    print(myStack)
    myStack.pop()
    print(myStack)
    myStack.pop()
    print(myStack)


# main function
def main():
    stack_s(myStack = [])  # function call


# main execution
if __name__ == '__main__':
    main()



