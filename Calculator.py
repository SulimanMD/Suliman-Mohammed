# Creating a simple calculator

# These are the options need to be select by the user
print ("Select the operation you want :-")
print (" 1- Addition")
print (" 2- Subtraction")
print (" 3- Multiplication")
print (" 4- Division")

# Addition Function
def Addition (num1, num2):
    return num1 + num2

# Subtraction Function
def Subtraction (num1, num2):
    return num1 - num2

# Multiplication Function
def Multiplication (num1, num2):
    return num1 * num2

# Division Function
def Division (num1, num2):
    return num1 / num2

# User input
List = "1 2 3 4"
print("Select your option",List.split(' '))
User_choice = input()

if User_choice in ("1","2","3","4") :
    # The two numbers to do the operation on
    Number1 = int ( input ("Enter your first number: "))
    Number2 = int ( input ("Enter your second number: "))
else: 
     print("Your choice is invalid try again")

# If statements for the choices

if User_choice == "1":
    print(Number1," + ",Number2," = ", Addition(Number1,Number2))
    
elif User_choice == "2":
    print(Number1," - ",Number2," = ", Subtraction(Number1,Number2))

elif User_choice == "3":
    print(Number1," * ",Number2," = ", Multiplication(Number1,Number2))

elif User_choice == "4":
    print(Number1," / ",Number2," = ", Division(Number1,Number2))
   
