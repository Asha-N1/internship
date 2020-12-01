# import required library
import mysql.connector

# creating class
class Database:
    # connecting database
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
    )
    mycursor =mydb.cursor()
    # function for create database
    def dbcreate(self):
        # query for creating databse
        Database.mycursor.execute("CREATE DATABASE Company")

    

# main function
def main():
    # class type object
    Database_obj = Database()
    # calling dbcreate function
    Database_obj.dbcreate()
    Database.mycursor.execute("SHOW DATABASES")
    for x in Database.mycursor:
        print(x)

    

# main execution
if __name__ == '__main__':
    main()
