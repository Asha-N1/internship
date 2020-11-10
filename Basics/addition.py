# This program adds two numbers
def addition(num1,num2):
    # Add two numbers
    sum = num1 + num2
    print("sum of " ,num1, " and ",num2, "=",sum)
   

# main function
def main():
    num1=int(input("enter num1:"))
    num2=int(input("enter num2:"))
    sum=addition(num1,num2)
   
    
# executing main function  
if __name__ == '__main__':
    main()


