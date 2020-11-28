# importing reqiured library
import mysql.connector

# creating class
class My_db:
    # defining function
    def my_db_fun(self):
        # connecting to database
        mydb = mysql.connector.connect( 
            host="localhost",
            user="root",
            password="",
            database="department"
        )
        mycursor = mydb.cursor()
        # query for inserting records
        sql = "INSERT INTO staff (name, address) VALUES (%s, %s)"
        # values to insert
        val = [
            ('suma','muragamalla'),
            ('sree', 'kerala'),
        ]
        mycursor.executemany(sql, val)
        # commiting changes to table
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")

# main function
def main():
    ob = My_db()
    ob.my_db_fun()

# main execution
if __name__ == "__main__":
	main()