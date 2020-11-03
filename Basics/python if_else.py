# checking given number is greater or not and also equals
a = 10
b = 10

if a>b:
    print("a is greater then b")
elif a == b:
    print("a equals to b")
else:
    print("a is not greater then b")

# given num is even or odd
x = 7
r = x % 2

if r == 0:
    print("even")
else:
    print("odd")

# Nested if statement
y = 20
z = 30
if y != z:
    print("y is not equal to z")
    if(y < z):
        print("y is lesser than z")
    else:
        print("y is not lesser then z")
