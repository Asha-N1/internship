# dictionaries in python
std1 = {                 # creating dictionary
    "name" : "asha",
    "address" : "bangalore",
    "usn" : "1DA19SCS05"
}
print(std1)
a = std1["name"]  # accessing item by key value
print(a)

b = std1.get("address") # same as above statement but we using get here
print(b)

print(len(std1))  # length of dictionary

std1["age"] = "24" # adding another item into dictionary
print(std1)

std1["name"] = "deeksha"
print(std1)

std1.pop("name") # deleting item name
print(std1)

std1.popitem() # delete last item in dictionary
print(std1)

student1 = std1.copy() # copying the dictionary
print(student1)

subjects = {            # nested dictionary
    "python" : {
     "author" : "Allen",
     "year" : 2004
    },
    "java" : {
     "author" : "sahani",
     "year" : 1980
    },
    "dbms" : {
     "author" : "xyz",
     "year" : 1986
    }
}
print(subjects)

subjects.clear() # clear the dictionary
print(subjects)
