# importing required library
import requests
# creating class 
class get_request:
    # creating function
    def get_request_fun(self):
        # Making a GET request 
        r = requests.get('https://www.google.com/') 
        
        # check status code for response received 
        # success code - 200 
        print(r) 
        
        # print content of request 
        print(r.content) 

# main function
def main():
    ob = get_request()
    ob.get_request_fun()

# main execution        
if __name__ == '__main__':
    main()