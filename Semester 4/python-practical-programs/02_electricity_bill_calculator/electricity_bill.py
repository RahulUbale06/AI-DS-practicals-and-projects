# 2. Write a Python program to calculate electricity bills using if-elif
# conditions based on unit consumption and store customer details
# in a dictionary.

customer_name = input("Enter Customer name: ")
units_consumption = int(input("Enter units consumption: "))

if units_consumption <= 100:
    rate_per_unit = 5
    bill = units_consumption * 5

elif units_consumption <= 200:
    rate_per_unit = 7
    bill = units_consumption * 7

else:
    rate_per_unit = 10
    bill = units_consumption * 10

customer_detail = {
    "name": customer_name,
    "units_consumed": units_consumption,
    "rate_per_unit": rate_per_unit,
    "total_bill": bill
}

print("========Customer Details=========")
print("Name:", customer_detail["name"])
print("Units Consumed:", customer_detail["units_consumed"])
print("Rate Per Unit:", customer_detail["rate_per_unit"])
print("Total Bill:", customer_detail["total_bill"])
