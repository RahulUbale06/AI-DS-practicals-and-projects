# 11. Write a Python program to write student details into a file
# and read them back using file handling operations.

print("*" * 40)
print("      STUDENT FILE SYSTEM")
print("*" * 40)

name = input("\nEnter student name: ")

age = int(input("Enter student age: "))

marks = float(input("Enter student marks: "))

# Writing into file
with open("student.txt", "w") as file:

    file.write("Student Details\n")
    file.write("-" * 20 + "\n")

    file.write(f"Name  : {name}\n")
    file.write(f"Age   : {age}\n")
    file.write(f"Marks : {marks}\n")

print("\nData written successfully.")

# Reading from file
with open("student.txt", "r") as file:

    content = file.read()

print("\nStored Student Details")
print("*" * 40)

print(content)

