# 9. Write a Python program to store student details in a tuple and
# display the details using tuple unpacking.

# Store student details in tuple
# and display using tuple unpacking

print("*" * 40)
print("      STUDENT DETAILS SYSTEM")
print("*" * 40)

# Taking student input
student_name = input("\nEnter student name: ")

student_age = int(input("Enter student age: "))

student_marks = float(input("Enter student marks: "))

# Creating tuple
student_details = (student_name, student_age, student_marks)

# Tuple unpacking
name, age, marks = student_details

# Displaying details
print("\n" + "*" * 40)
print("        STUDENT DETAILS")
print("*" * 40)

print(f"Name  : {name}")
print(f"Age   : {age}")
print(f"Marks : {marks}")

print("*" * 40)