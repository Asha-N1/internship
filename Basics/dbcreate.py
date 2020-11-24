# importing rquired libraries 
import mysql.connector 

# class DB_connection
class DB_connection:
  def db_fun(self): # function db_fun
    dataBase = mysql.connector.connect( 
      host ="localhost", 
      user ="root", 
      passwd =""
    ) 
    # preparing a cursor object 
    cursorObject = dataBase.cursor() 
  
    # creating database 
    cursorObject.execute("CREATE DATABASE Customer") 

# main function
def main():
  ob = DB_connection()
  ob.db_fun()
  
# main execution
if __name__ == '__main__':
  main()
