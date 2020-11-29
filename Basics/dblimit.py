# import library
import mysql.connector

# classs for delete
class Dblimit:
    # function defination
    def dblimit_fun(self):
        # database connection
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "department"
        )
        mycursor = mydb.cursor()
        # query for limit
        mycursor.execute("SELECT * FROM customers LIMIT 5")
        # fetching content from table
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

# main function
def main():
    ob = Dbdelete()
    ob.dbdelete_fun()

# main execution
if __name__ == '__main__':
    main()
    

