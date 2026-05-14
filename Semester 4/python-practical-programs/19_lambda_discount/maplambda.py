# 19. An e-commerce website wants to apply a 10% discount to
# all product prices in a list using map() and lambda.

prices = list(map(float,input("Enter product prices separated by space: ").split()))
discounted_price = list(map(lambda price: price-(price*0.10),prices))
print(prices)
print(discounted_price)