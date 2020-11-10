# dictionaries in python

# function defination
def dict_student(dict):
    print("dictionary:",dict)

# function for updating dictionary
def dict_student_update(dict):
    print("updated dictionary:",dict)

# function for insert value to dictionary
def dict_student_insert(dict):
    print("new value is inserted to name in dictionary:",dict)

# function for finding key in dictionary
def dict_student_find(dict):
    if dict:
        print("name found")
    else:
        print("name not found") 

# main function
def main():
    dict = {'name': 'asha','age':'24','branch':'cse','marks':'8.2'} # creating dictionary
    dict_student(dict)

    dict2= {'usn':'1da19scs05'} 
    dict.update(dict2) # update method
    dict_student_update(dict)

    dict['name']="deeksha" # inserting value to name key
    dict_student_insert(dict)

    dict.get('name')        # it will find name key is present in dictionary or not
    dict_student_find(dict)


# main function execution 
if __name__ == '__main__':
    main()





