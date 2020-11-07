#  Inheritance in python
class Parent:     # creating class parent
    def func1(self):    # fun1 method
        print("this is parent class")

class child(Parent): # Inheriting the parent class
    def func2(self):    # init method
        print("this is child class")

ob = child() # creating child type object
ob.func1()   # calling methods of parent class
ob.func2()   # calling methods of parent class

# init function in python

class P1:  #
    def __init__(self,fname,fage): # passing arguments
        self.name = fname
        self.age = fage

    def view(self):
        print(self.name,self.age)
# overriding the parent class init method
class child(P1):
    def __init__(self,fname,fage):
        P1.__init__(self, fname,fage)
        self.lastname = "ammu"

    def view(self):
        print(self.age, self.lastname, self.name)

ob = child(23, 'python')
ob.view()

# single Inheritance
class A: # creating
    def f1(self):
        print("print class a")

class B(A): # Inheritance parent class
    def f2(self):
        print("print class b")
x = B()
x.f1()

# mutliple  inheritence

class X: # creating class X
    def f1(self):
        print("print class a")

class Y: # creating class Y
    def f2(self):
        print("print class b")

class Z(X,Y): # Inheritance class X and Y
    def f3(self):
        print("print class b")

obj = Z()
obj.f1()
obj.f3()


