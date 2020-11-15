#  Inheritance in python
class Parent:     # creating class parent
    def func1(self):    # fun1 method
        print("this is parent class")

class child(Parent): # Inheriting the parent class
    def func2(self):    # init method
        print("this is child class")

# mutliple  inheritence
class python: # creating class X
    def f1(self):
        print("print class python")

class php: # creating class Y
    def f2(self):
        print("print class php")

class java(python,php): # Inheritance class X and Y
    def f3(self):
        print("print class java")

# single Inheritance
class parent_3: # creating
    def f1(self):
        print("print class parent")

class child_3(parent_3): # Inheriting parent class
    def f2(self):
        print("print class child")

class Parent_4:  # parent class
    def __init__(self,fname,fage): # constructor
        self.name = fname
        self.age = fage

    def view(self):
        print(self.name,self.age)
# overriding the parent class init method
class child_4(Parent_4):
    def __init__(self,fname,fage):
        Parent_4.__init__(self, fname,fage) 
        self.lastname = "ammu"

    def view(self):
        print(self.age, self.lastname, self.name)



# main function
def main():
    obj = child() # creating child type object
    obj.func1()   # calling methods of parent class
    obj.func2()   # calling methods of parent class
    obj1 = java() # java class object
    obj1.f1()     # inheriting python class in java
    obj1.f3()     # inheriting php class in java
    obj1.f2()     # calling object of java class
    obj2 = child_3()
    obj2.f1()
    obj2.f2()
    ob = child_4(23, 'python')
    ob.view()


# main execution
if __name__ == '__main__':
    main()










