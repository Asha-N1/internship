# importing library
import mysql.connector

# class for database operations

class Dboperations:
    # database connection
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "Company"     
    )
    mycursor = mydb.cursor()
    # function defination
    def createtable(self):
        # query for creating table
        Dboperations.mycursor.execute("CREATE TABLE Employee (Name varchar(30), Address varchar(30), salary varchar(20), ssn varchar(30))")
    def insertvalues(self):
        # query for inserting records
        sql = "INSERT INTO Employee (Name, Address, salary, ssn) VALUES (%s, %s, %s, %s)"
        # values to insert
        val = [
            ('asha','muragamalla','50000','E1'),
            ('sree', 'selam','10000','E11'),
            ('jaanu','bihar','20000','E10'),
            ('anil', 'kerala','10000','E3'),
            ('anusha','bangalore','50000','E4'),
            ('naveen', 'kerala','10000','E5'),
            ('asha','chintamani','50000','E6'),
            ('maitra', 'mysore','10000','E7'),
            ('deeksha','kochi','60000','E8'),
            ('shivu', 'kerala','10000','E9'),
        ]
        Dboperations.mycursor.executemany(sql,val)
        

# main function
def main():
    Dboperations_obj = Dboperations()
    Dboperations_obj.createtable()
    Dboperations_obj.insertvalues()
    # commiting changes to table
    Dboperations.mydb.commit()
    print(Dboperations.mycursor.rowcount, "was inserted.")
    Dboperations.mycursor.execute("SELECT * FROM Employee")
    myresult = Dboperations.mycursor.fetchall()
    for x in myresult:
        print(x)

# main execution
if __name__ == "__main__":
	main()