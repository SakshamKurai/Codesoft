print("Welcome to Codsoft calculator")

x = ("+  -  *  /")
print("function available in calculator is : "  )
print(x)

num1 = int(input( "Enter your 1st number  \n"))
operation = input("Enter your operation \n")
num2 = int(input("Enter your 2nd number \n"))

if operation is "+" :
    print( "Sum of both number is ", num1 + num2) 
elif operation is "-":
    print("Difference of both number is ", num1-num2)
elif operation is "*" :
    print("Product of both number is ", num1*num2)
elif operation is "/" :
    print("Division of number 1 by number 2 is ", num1/num2)
    
else :
    print("Operation entered is not available")
    
print("Thanks for using Codsoft calculator ")