# 8. Create a Polynomial Model for Car Mileage
# Build a polynomial regression model to predict mileage based on car speed or engine
# size.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

x = np.array([1,2,3,4,5]).reshape(-1,1)

y = np.array([2,4,8,16,32])

poly = PolynomialFeatures(degree=2)

x_poly = poly.fit_transform(x)

model = LinearRegression()

model.fit(x_poly, y)

plt.scatter(x, y)

plt.plot(x, model.predict(x_poly))

plt.xlabel("Engine Size")

plt.ylabel("Mileage")

plt.show()