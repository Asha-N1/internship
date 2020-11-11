# string methods

# convert string to uppercase
def str_upper(mystring):
    print(mystring.upper()) # uppercase method

# convert string to lowercase
def str_lower(mystr):
    print(mystr.lower()) # lowercase

# reverse string
def str_reverse(mystring):
    print(mystring[::-1]) # string reverse

# join string
def join_str(seq):
    s1 ="+"
    print(s1.join(seq)) # join method

# replace string
def replace_str(mystring):
    rpl_str=mystring.replace("python","java") # replace method
    print(rpl_str)

# split string
def split_str(mystring):
    print(mystring.split()) # split method

# main function
def main():
    mystring = "welcome to python programming" # string
    mystr = "WELCOME TO PYTHON PROGRAMMING"
    seq = "welcome","to","python","programing"
    str_upper(mystring) # calling upper function
    str_lower(mystr)    # calling lower function
    str_reverse(mystring) # calling reverse function
    join_str(seq)         # calling join function
    replace_str(mystring) # calling replace function
    split_str(mystring)   # calling split function

if __name__ == '__main__':
    main()




