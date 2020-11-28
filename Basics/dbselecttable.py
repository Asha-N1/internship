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
        mycursor.execute("select * from admin")
        myresult = mycursor.fetchall()
        for i in myresult:
            print(i)

# main function
def main():
    ob = Ctable()
    ob.ctable()

# main execution
if __name__ == "__main__":
	main()