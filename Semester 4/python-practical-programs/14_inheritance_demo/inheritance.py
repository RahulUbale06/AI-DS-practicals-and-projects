# 14. Write a Python program to demonstrate inheritance using a
# Person class and Student subclass with method overriding.
# Inheritance Program

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):

        print("\nPerson Details")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):

    def __init__(self, name, age, course):

        super().__init__(name, age)

        self.course = course

    # Method overriding
    def display(self):

        print("\nStudent Details")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")


# Input
name = input("Enter student name: ")

age = int(input("Enter age: "))

course = input("Enter course: ")

# Object
student = Student(name, age, course)

student.display()