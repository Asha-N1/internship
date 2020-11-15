# scope in python
a = 10 # Global variable anywhere we can access
def myfunction(): # defining function
    a = 20 # local variable with in function
    print(a) # printing local
print(a) # printing global


# changing local to global
x = 90
def something():
    global x # changing to global
    x = 67
    print(x)

# accessing global variable
v = 19
m = 56
def num():
    u = 45
    c = globals() ['v'] # accessing global
    print(c)
    globals()['m'] = 78 # changing global variable

# main function
def main():
    myfunction()
    print(a) # printing global
    something()
    print(x)
    num()
    print(v)
    print(m)



# main execution
if __name__ == '__main__':
    main()




