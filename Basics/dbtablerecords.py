# importing library
import mysql.connector

# creating class
class DB_show:
	def db_show_fun(self):
		mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="asbs")
		mycursor = mydb.cursor()
		mycursor.execute("select * from bills")
		for i in mycursor:
			print(i)

# main function
def main():
  ob = DB_show()
  ob.db_show_fun()


  
# main execution
if __name__ == '__main__':
  main()