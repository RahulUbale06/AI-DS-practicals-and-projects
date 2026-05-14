# 20. Create a dictionary named student with attributes name,
# age, and marks, then perform basic operations like accessing the
# name, updating marks, and adding a new attribute grade based
# on marks
# Student Dictionary Operations

student = {
    "name": "Rahul",
    "age": 19,
    "marks": 85
}

# Accessing name
print("Student Name :", student["name"])

# Updating marks
student["marks"] = 90

print("Updated Marks :", student["marks"])

# Adding grade
if student["marks"] >= 90:

    student["grade"] = "A"

elif student["marks"] >= 75:

    student["grade"] = "B"

else:

    student["grade"] = "C"

# Final dictionary
print("\nFinal Student Dictionary")

for key, value in student.items():

    print(f"{key} : {value}")