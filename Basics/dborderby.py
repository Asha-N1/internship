# import required library
import mysql.connector

# create class
class Dborderby:
    # function defination
    def dborderby_fun(self):
        # database connection
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="department"
        )
        mycursor = mydb.cursor()
        # query for orderby
        sql = "SELECT * FROM customers ORDER BY name"

        mycursor.execute(sql)
        # fetching content
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

# main function
def main():
    ob = Dborderby()
    ob.dborderby_fun()

# main execution        
if __name__ == '__main__':
    main()