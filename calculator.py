num1= float(input("Enter your first number:"))
op=  input("enter your operator:")
num2= float(input("enter the second number:"))
if op == "+":
    print( num1+num2 )
elif op == "-":
    print( num1-num2 )
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid")