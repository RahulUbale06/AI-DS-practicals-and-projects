# 13. Write a Python program to create a class Student with
# attributes and methods to display student information and
# percentage.
# Student Class Program

class Student:

    # Constructor
    def __init__(self, name, roll_no, marks):

        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Method to calculate percentage
    def calculate_percentage(self):

        return (sum(self.marks) / len(self.marks))

    # Method to display details
    def display_details(self):

        print("\n" + "*" * 40)
        print("        STUDENT DETAILS")
        print("*" * 40)

        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_no}")
        print(f"Marks      : {self.marks}")

        print(f"Percentage : {self.calculate_percentage():.2f}%")


# Input section
name = input("Enter student name: ")

roll_no = int(input("Enter roll number: "))

marks = list(map(float, input("Enter marks separated by space: ").split()))

# Object creation
student1 = Student(name, roll_no, marks)

# Method call
student1.display_details()