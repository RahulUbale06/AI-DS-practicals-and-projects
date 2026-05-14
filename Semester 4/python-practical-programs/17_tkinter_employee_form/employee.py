# 17. Write a Python Tkinter GUI program to accept employee
# details and display them using labels or message boxes.
# Employee Details GUI

# Employee Details GUI

import tkinter as tk
from tkinter import messagebox

# Function
def show_details():

    name = entry_name.get()

    emp_id = entry_id.get()

    department = entry_department.get()

    messagebox.showinfo(
        "Employee Details",
        f"Name : {name}\n"
        f"ID : {emp_id}\n"
        f"Department : {department}"
    )


# Window
root = tk.Tk()

root.title("Employee Management")

root.geometry("300x250")

# Labels
tk.Label(root, text="Employee Name").pack()

entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Employee ID").pack()

entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Department").pack()

entry_department = tk.Entry(root)
entry_department.pack()

# Button
tk.Button(root, text="Submit", command=show_details).pack(pady=10)

root.mainloop()