# 7. Write a Python program to store employee details in a dictionary
# and display employees with salary greater than a given amount.

employee_details = {}

print("*" * 40)
print("      EMPLOYEE MANAGEMENT SYSTEM")
print("*" * 40)

employee_num = int(input("\nEnter number of employees: "))

# Taking employee details
for i in range(employee_num):

    print(f"\nEnter details for Employee {i+1}")

    employee_name = input("Enter employee name: ")

    employee_salary = float(input("Enter employee salary: "))

    employee_details[employee_name] = employee_salary

# Salary limit input
salary_limit = float(input("\nEnter salary limit: "))

print("\n" + "*" * 40)
print(f"Employees having salary greater than {salary_limit}")
print("*" * 40)



# Filtering employees
for employee_name, salary in employee_details.items():

    if salary > salary_limit:

        print(f"{employee_name} : {salary}")



