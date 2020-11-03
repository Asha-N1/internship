# classes and objects in python
class Myclass: # defining class
    def config(self): # defining config method
        print("i5,8GB,1TB")
com1 = Myclass() # creating object com1

print(type(com1)) # displaying type of object

com1.config() # calling object



# another example of classes and objects

class Student: # class student
    pass
s1 = Student() # creating objects
s2 = Student()

s1.first = 'asha' # instance variables
s1.last =' N'
s1.marks = '76'

s2.first = 'deeksha'
s2.last =' v'
s2.marks = '98'

print(s1.first) # calling manually objects
print(s2.first)

# using initialized methods
class Stu:
    def __init__(self,first,last,marks): # init method
        self.first = first # assigning to self arguments
        self.last = last
stu1 = Stu('shiva','n','89') # creating object and passing values
stu2 = Stu('raju','b','67')
print(stu1.last)
print(stu2.last)
print('{} {} '.format(stu1.last, stu2.last))









