# program for connecting youtube using socket 

# importing socket lobrary
import socket
import sys

# socket class
class Sockets:
    def soc_fun(self): # function for sockets
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("socket successfully created")
        except socket.error as err:
            print("socket creation failed with error %s" %(err))
        
        # default port for socket
        port = 80
        try:
            host_ip = socket.gethostbyname('www.youtube.com') 
        except socket.gaierror: 
  
        # this means could not resolve the host 
            print("there was an error resolving the host")
            sys.exit() 
  
        # connecting to the server 
        s.connect((host_ip, port)) 
  
        print("the socket has successfully connected to youtube \ on port == %s" %(host_ip)) 

def main():
    ob = Sockets()
    ob.soc_fun()

if __name__ == '__main__':
    main()

