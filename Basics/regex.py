# RegEx in python
import re # importing re module

# checking given email is valid or not

def validate_email(email): # function for email
  return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$',email) # pattren for checking email

email = input("enter the email:") # providing email
valid =validate_email(email)  # calling function
if valid:                     # checking valid
  print(email, 'is correct')  # format correct
else:
  print('invalid email format:', email) # format incorrect


# checking given pincode is valid or not

def validate_pincode(pincode):
  return re.findall('^[1-9][0-9]{5}$', pincode)

pincode = input("enter the pincode belongs to india:") # providing email
valid =validate_pincode(pincode)  # calling function
if valid:                     # checking valid
  print(pincode, 'is correct')  # format correct
else:
  print('invalid pincode format:', pincode) # format incorrect


def validate_website(url):
  return re.findall('((http|https)://)(www.)?', url)

url = input("enter the website url:") # providing email
valid=validate_website (url)  # calling function
if valid:                     # checking valid
  print(url, 'is correct')  # format correct
else:
  print('invalid website format:', url) # format incorrect
