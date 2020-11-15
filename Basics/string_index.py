# display of string index

# main function
def main():
    name= "python program"
    print(name[5]) # index of 5

    #python substring and slicing of string

    a = "python is easy to learn and understand"
    print(a[0:5]) # slicing of string
    print(a[:10]) # only proving end index
    print(a[10:]) # only providing starting index
    print(a[:])   # display whole string slice
    print(a[0:10:2]) # specifying steps 2
    print("\n")

    # reversing of string

    print(a[::-1])
    print('\n')

    print(a[-5:-2]) # providing negative index

# main execution
if __name__ == '__main__':
    main()
