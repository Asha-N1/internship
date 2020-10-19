# scope in python
a = 10 # Global variable anywhere we can access

def myfunction(): # defining function
    a = 20 # local variable with in function

    print(a) # printing local

myfunction()

print(a) # printing global


# changing local to global

x = 90

def something():
    global x # changing to global
    x = 67
    print(x)

something()
print(x)

# accessing global variable
v = 19
m = 56
def num():
    u = 45
    c = globals() ['v'] # accessing global
    print(c)
    globals()['m'] = 78 # changing global variable

num()
print(v)
print(m)




