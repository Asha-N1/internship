# static and instant variables


# student class
class student:
    clg_name = "AIT" # static variable
    def __init__(self): # constructor
        self.name = "Asha"    # instance variable inside constructor
        print("Student name",self.name) # accessing instance variable inside constructor
        student.branch = "cse" # static variable
    def display(self):
        self.clg_loc = "Bangalore"  # instance variable inside method
        print("Collage location:",self.clg_loc) # accessing instance variable inside method

# main function
def main():
    std=student() # object for class
    print("Collage name:",student.clg_name) # accessing static variable inside class
    print("Branch:",student.branch) # accessing static variable inside constructor
    std.display() # calling display method
    
# main execution
if __name__ == '__main__':
    main()

    
    



