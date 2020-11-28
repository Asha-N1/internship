# importing library
import mysql.connector

# class
class Ctable:
    # function defination
    def ctable(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "collage"
            
        )
        mycursor = mydb.cursor()
        # query for creating table
        mycursor.execute("CREATE TABLE departments (cse varchar(20), me varchar(10), ec varchar(40))")

# main function
def main():
    ob = Ctable()
    ob.ctable()

# main execution
if __name__ == "__main__":
	main()