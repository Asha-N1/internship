# Convert from one type to another:

# main function
def main():
    num1 = 10    # int
    num2 = 20.8  # float
    num3 = 3j   # complex

    # convert from int to float:
    val1 = float(num1)

    # convert from float to int:
    val2 = int(num2)

    # convert from int to complex:
    val3 = complex(num3)

    print(val1)
    print(val2)
    print(val3)

    print(type(val1))
    print(type(val2))
    print(type(val3))

# main execution
if __name__ == '__main__':
    main()