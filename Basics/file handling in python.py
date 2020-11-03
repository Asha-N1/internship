# File handling in python


f = open("content.txt", "r") # opening file in read mode
print(f.readline())
print(f.read(4)) # first 4 characters from file
print(f.read()) # reading file

f = open("content.txt", "a")
f.write("Now the file has more content!") # appending content into file
f.close()

# open and read the file after the appending:
f = open("content.txt", "r")
print(f.read())


f = open("4.txt", "x") # creating file

f = open("content.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("content.txt", "r")
print(f.read())

