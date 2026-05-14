# 12. Write a Python program to implement a calculator (all
# operations) using exception handling for division by zero and
# invalid input.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("ENter operation ( +,-,*,/) : ")
try:
    if operation == "+":
        result = num1 + num2
        print(result)
    elif operation == '-':
        result = num1 - num2
        print(result)
    elif operation == '*':
        result = num1 * num2
        print(result)
    elif operation == '/':
        result = num1 / num2
        print(result)
    else:
        print("Invalid operation")

except ZeroDivisionError:
    print("cannot be divided by zero")
except TypeError:
    print("Invalid operation")
