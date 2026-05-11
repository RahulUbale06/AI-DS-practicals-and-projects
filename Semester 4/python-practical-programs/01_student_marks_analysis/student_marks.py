# 1. Write a Python program to accept marks of students in a list and
# calculate total, average, highest, and lowest marks using loops
# and conditional statements.

n = int(input("Enter the number of students: "))
marks = []
for i in range(n):
    mark = float(input(f"Enter the marks of student {i+1}: "))
    marks.append(mark)

Total = 0
highest = marks[0]
lowest = marks[0]

for mark in marks:

    Total += mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

avg = Total / n

print("========Result=========")
print(f"Total marks: {Total}")
print(f"Average marks: {avg}")
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}")
