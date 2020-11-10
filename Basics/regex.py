# RegEx in python
# importing re module
import re 

# function to check the given email is valid or not
def validate_email(email): # function for email
  return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$',email) # pattren for checking email

# function to check the given website url is valid or not
def validate_website(url):
  return re.findall('((http|https)://)(www.)?', url)


# function to check the given pincode is valid or not
def validate_pincode(pincode):
  return re.findall('^[1-9][0-9]{5}$', pincode)


# main function 
def main():
    email = input("enter the email:") # providing email
    valid =validate_email(email)  # calling function
    if valid:                     # checking valid
        print(email, 'is correct')  # format correct
    else:
        print(email, 'is invalid') # format incorrect
    
    url = input("enter the website url:") # providing email
    valid=validate_website (url)  # calling function
    if valid:                     # checking valid
      print(url, 'is correct')  # format correct
    else:
      print(url,'is invalid') # format incorrect
    
    pincode = input("enter the pincode belongs to india:") # providing email
    valid =validate_pincode(pincode)  # calling function
    if valid:                     # checking valid
      print(pincode, 'is correct')  # format correct
    else:
      print(pincode,'is invalid') # format incorrect




# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()