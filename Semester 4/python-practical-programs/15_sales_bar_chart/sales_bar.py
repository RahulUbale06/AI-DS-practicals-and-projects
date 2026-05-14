# 15. Write a Python program using NumPy arrays to store
# monthly sales data and display a bar chart using Matplotlib.
import numpy as np
import matplotlib.pyplot as plt

months = np.array([
    "Jan", "Feb", "Mar",
    "Apr", "May", "Jun"
])
sales = np.array([5000, 7000, 6500, 8000, 9000, 7500])
plt.bar(months, sales)
plt.title("Sales Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
