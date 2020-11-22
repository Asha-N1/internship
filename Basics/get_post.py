# get, post, put and delete methods

# importing request library
import requests

# creating class Get_method
class Get_method:
    def get_fun(self): # function get_fun
        r = requests.get('https://docs.python.org/3/download.html') # using get method
        print("from get method:")
        print(r.text[:500]) # display first 500 characters from that given url
        print("\n")
# creating class Post_method
class Post_method:
    def post_fun(self): # function post_fun
        my_url = 'https://postman-echo.com/post'
        myparams = {'email':'a@gamil.com','name':'asha','phone':'9353742509'}
        res = requests.post(my_url,data=myparams) # using post method
        print("from post method:\n")
        print(res.text) 
        print("\n")

class Put_method:
    def put_fun(self): # function post_fun
        myurl = 'https://postman-echo.com/put'
        myparams = {'email':'a@gamil.com','name':'asha','phone':'9353742509'}
        res = requests.put(myurl, data=myparams)
        print("from put method:\n")
        print(res.text)
        print("\n")

class Delete_method:
    def delete_fun(self): # function post_fun
        myurl1 = 'https://postman-echo.com/delete'
        res1 = requests.delete(myurl1, data="testing delete")
        print("from delete method:\n")
        print(res1.text)
        

# main function
def main():
    ob = Get_method() # creating class type object
    ob.get_fun()      # calling function
    ob1 = Post_method()
    ob1.post_fun()
    ob2=Put_method()
    ob2.put_fun()
    ob3=Delete_method()
    ob3.delete_fun()

    
# main execution
if __name__ == '__main__':
    main()