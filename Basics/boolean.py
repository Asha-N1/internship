# boolean in python

# main function
def main():
    python = True
    print(type(python))  # display type of a
    x = 10
    y = 20
    c = 30
    print(x > y) # checking x greater than y
    print(x < y) # checking x lesser than y

    num1 = 20
    num2 = 30
    print(num1>=num2) # greater then or equals too
    print(num1==y) # both are equals
    print(num1!=num2) # not equals
    print(x>y) or print(y>c) # logical OR condition
    print(x>y) and print(y>c) # logical AND condition
    print(not(x>y)) # logical NOT condition

    # Evaluation of variables
    print(bool("Hello"))
    print(bool(15))
    print(bool())
    print(bool(int))

# main execution
if __name__ == '__main__':
    main()




