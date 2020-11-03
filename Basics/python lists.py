# Lists in python

names = ["asha","deeksha","rajesh","shiva"] # creating list
print(names)
print(names[:3]) # upto position 3
print(names[2:]) # it display from position 2
print(names[-2:-1]) # accessing from negative index
print(names[1:3]) # specifying range
print(names[1]) # accessing position 1 element in list
print(len(names))

names[2] = "jaanu" # adding item to list at position 2
print(names)

# methods in list
names.append("anil") # adding item to list
print(names)

names.insert(1,"ammu") # inserting element at position 1
print(names)

names.reverse() # displaying list reverse
print(names)

names.pop() # pop last item in list
print(names)

del names[1] # deleting item 1 from list
print(names)


names.clear() # clearing items from list
print(names)

list1 = ["1","2","3","4"]
list2 = ["a","b","c"]
list3 = list1 + list2 # adding two list
print(list3)






