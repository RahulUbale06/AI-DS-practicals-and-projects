# 16. Write a Python program using NumPy and Matplotlib to
# store student marks and display a line graph of marks.
# Student Marks Line Graph

import numpy as np
import matplotlib.pyplot as plt

students = np.array([1, 2, 3, 4, 5])

marks = np.array([75, 80, 68, 90, 85])

plt.figure(figsize=(8, 5))

plt.plot(students, marks, marker="o")

plt.title("Student Marks Graph")

plt.xlabel("Student Number")

plt.ylabel("Marks")

plt.grid(True)

plt.show()