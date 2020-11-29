# import library
import mysql.connector

# classs for delete
class Dbupdate:
    # function defination
    def dbupdate_fun(self):
        # database connection
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "department"
        )
        mycursor = mydb.cursor()
        # query for update
        sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

        mycursor.execute(sql)
        # commit the changes to table
        mydb.commit()

        print(mycursor.rowcount, "record(s) updated")

# main function
def main():
    ob = Dbupdate()
    ob.dbupdate_fun()

# main execution
if __name__ == '__main__':
    main()
    