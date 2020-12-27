# Import socket module 
import socket                

# class client
class Client:
    def client_fun(self): # function client
        s = socket.socket()  # Create a socket object         
        port = 1234 # Define the port on which you want to connect 
        s.connect(('127.0.0.1', port)) # connect to the server on local computer 
        response =  s.recv(1024) # receive data from the server 
        data=response.decode()
        print(data) 
        
        # close the connection 
        s.close()       

# main function
def main():
    ob = Client() # class type object
    ob.client_fun() # calling function

# main execution
if __name__ == '__main__':
    main()