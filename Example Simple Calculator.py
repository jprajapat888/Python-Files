# Example: Simple Calculator
# Before we wrap up this lession, let's create a program that can perform addition, subtraction, multiplication and divison based on the input from the user.

print("what operation do you want?") 

operator = input("Enter either +, -, *, or divide: ")

n1 = float(input("Enter first number: "))

n2 = float(input("Enter second number: "))

if operator == "+":
    print(n1, operator, n2, "=", n1+n2)

elif operator == "-":
    print(n1, operator, n2, "=", n1-n2)

elif operator == "*":
    print(n1, operator, n2, "=", n1*n2) 

elif operator == "/":
    print(n1, operator, n2, "=", n1/n2) 

else: 
    print("Invalid operator")   