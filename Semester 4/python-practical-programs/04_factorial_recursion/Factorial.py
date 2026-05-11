# 4. Write a Python program to calculate factorial of a number using
# a recursive function.

num = int(input("Enter the number: "))
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(num))
