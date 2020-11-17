# delete in python
import os
# delete user defined class or objects
# defining class name Myfun
class Myfun:
    def delete_fun(self): # defining function 
        print("welcome to python programing")
#del Myfun # deleting class 

# delete variables, list, dictionary
class MyClass:
    def fun(self):
        myclass_v = "asha" # variable
        my_list = ('asha' ,'vani') # list
        my_dict = {'name':'asha', 'address':'bangalore'} # dictionary
        print(myclass_v)
        print(my_list)
        print(my_dict)

# delete file
class MyFile:
    def myfile_fun(self):
        os.remove("asha.txt") #delete file


# main function
def main():
    ob=Myfun() # creating class type object
    ob.delete_fun() # calling class function
    ob1=MyClass()
    ob1.fun()
    ob2=MyFile()
    ob2.myfile_fun()


   
# main execution
if __name__ == '__main__':
    main()


