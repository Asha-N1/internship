# File operations 

# open file

# function for file open
# file read
def file_open():
    file = open("text.txt")  # opening file text.txt 
    print(file.read()) # reading file

# file write
def file_write():
    with open("content.txt", "w") as fh:  # opening file context.txt
       print(fh.write("I love Python!!") )  

# main function
def main():
    file_open()
    file_write()  

# executing main
if __name__ == '__main__':
    main()

