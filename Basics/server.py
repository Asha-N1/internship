# client server program using scoket

# import socket
import socket

# class client_server
class Client_Server:
    def client_Server_fun(self): # function client_server
        s = socket.socket() # socket object
        print("socket created successfully")
        port = 5000 
        s.bind(('', port))         # bind method
        print("socket binded to %s" %(port))
        s.listen(5)   # put the socket into listening mode    
        print("socket is listening")            
        while True: # a forever loop until we interrupt it or  
            c, addr = s.accept()       # Establish connection with client. 
            print('Got connection from', addr) 
  
            # send a thank you message to the client.  
            response = "Thank you for connecting" 
            data=response.encode()
            c.send(data) 
  
            # Close the connection with the client 
            c.close() 

# main function
def main():
    ob = Client_Server() # class type object
    ob.client_Server_fun() # calling function

# main execution
if __name__ == '__main__':
    main()




