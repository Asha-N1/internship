# import library
import mysql.connector

# class for drop
class Droptable:
    # function for drop table
    def droptable_fun(self):
        # database connection
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "collage"
        )
        mycursor = mydb.cursor()
        # query for drop table
        sql = "DROP TABLE admin"

        mycursor.execute(sql)
    

        

# main function
def main():
    ob = Droptable()
    ob.droptable_fun()

# main execution
if __name__ == '__main__':
    main()
    



