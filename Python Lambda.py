# lambda in python
x = lambda a : a + 10 # add 10 to argument a
print(x(5))

x = lambda a, b : a * b # Multiply argument a with argument b
print(x(5, 6))

x = lambda a, b, c : a + b + c # Summarize argument a, b, and c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n # argument will be multiplied with an unknown number

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#
def myfunc(n): # same function definition to make both functions
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))