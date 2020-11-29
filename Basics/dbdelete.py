# import library
import mysql.connector

# classs for delete
class Dbdelete:
    # function defination
    def dbdelete_fun(self):
        # database connection
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "department"
        )
        mycursor = mydb.cursor()
        # query for delete
        sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

        mycursor.execute(sql)
        # commit the changes to table
        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted")

# main function
def main():
    ob = Dbdelete()
    ob.dbdelete_fun()

# main execution
if __name__ == '__main__':
    main()
    