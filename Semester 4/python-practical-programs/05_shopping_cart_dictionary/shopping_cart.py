# 5. Write a Python program to create a shopping cart using
# dictionary and calculate the total bill with discount conditions.


shopping_cart = {}

print("*" * 40)
print("      WELCOME TO SHOPPING CART")
print("*" * 40)

items = int(input("\nEnter number of products: "))

for i in range(items):

    print(f"\nEntering details for Product {i+1}")

    product = input("Enter product name: ")

    quantity = int(input("Enter quantity: "))

    price = float(input("Enter price per item: "))

    shopping_cart[product] = {
        "quantity": quantity,
        "price": price
    }
total_bill = 0
for product,details in shopping_cart.items():
    quantity = details["quantity"]
    price = details["price"]
    total_bill += quantity * price

discount =0
if total_bill >5000:
    discount = total_bill * 0.20
    total_bill = total_bill - discount
    print("Congratulations! You got a dicount of 20 %")
elif total_bill >2000:
    discount= total_bill * 0.10
    total_bill = total_bill - discount
    print("Congratulations! You got a dicount of 10 %")
else:
    print("You got no discount")

print("\n" + "*" * 30)
print("      SHOPPING CART")
print("*" * 30)

for product, details in shopping_cart.items():

    print(f"\nProduct : {product}")
    print(f"Quantity : {details['quantity']}")
    print(f"Price : {details['price']}")

print("\n" + "*" * 30)
print(f"Original Total Bill : {total_bill + discount}")

print(f"Discount Applied : {discount}")

print(f"Final Bill : {total_bill}")

print("*" * 30)