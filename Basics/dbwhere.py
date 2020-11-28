# import required library
import mysql.connector
# class
class Dbwher:
    # function defination
    def dbwhere_fun(self):
        # database connection
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="department"
        )

        mycursor = mydb.cursor()
        # query to select customer table
        sql = "SELECT * FROM customers WHERE name = 'vicky'"

        mycursor.execute(sql)
        # fetch content from table
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

# main function
def main():
    ob = Dbwher()
    ob.dbwhere_fun()

# main execution
if __name__ == "__main__":
	main()