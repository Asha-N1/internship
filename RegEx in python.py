# RegEx in python
import re # importing re module

#Check if the string starts with "The" and ends with "Spain":

txt = "is python programing language"
x = re.search("^is.*language$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

#Return a list containing every occurrence of "ai":

a = "The rain in Spain"
b = re.findall("ai", a)
print(b)

b = re.search("\s", a)

print("The first white-space character is located in position:", b.start()) # returns string first while space position


b = re.split("\s", a) # splitting string
print(b)

b = re.sub("\s", "1", a) # inserting 1 after  every word in string
print(b)