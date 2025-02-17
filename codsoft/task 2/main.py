# calculator
print("A calculator for simple arithematic operations of two numbers")
print("-"*20)
print("for addition use (+)")
print("for subtraction use (-)")
print("for multiplication use (*)")
print("for division use (/)")
print("-"*20)


a = int(input("Enter the first number: "))
optor = input("Enter the operator: ")
b = int(input("Enter the second number: "))

if(optor == "+"):
    print("The Addition of the two numbers is: ", a + b)
elif(optor == "-"):
    print("The Subtraction of the two numbers is: ", a - b)
elif(optor == "*"):
    print("The Multiplication of the two numbers is: ", a * b)
elif(optor == "/"):
    if(b != 0):
        print("The Division of the two numbers is: ", a / b)
    elif(b == 0):
        print("Error! Division by zero is not allowed")
else:
    print("Error! Invalid operator")
    print("please use one of the following operators: +, -, *, /")

