# 3. Write a Python program to check whether a number is prime

def check_prime(num):
    if num <2:
        print("not prime")
        return

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("prime")
    else:
        print("not prime")

number = int(input("Enter a number: "))
check_prime(number)
