# Lists in python

names = ("asha","deeksha","rajesh","shiva") # creating list
print(names)
print(names[:3]) # upto position 3
print(names[2:]) # it display from position 2
print(names[-2:-1]) # accessing from negative index
print(names[1:3]) # specifying range
print(names[1]) # accessing position 1 element in tuple
print(len(names))

y = list(names) # converting to list
y[1] = "anu"
names = tuple(y)
print(names)

x = ("a","v","f")
z = names + x # adding two tuples
print(z)



