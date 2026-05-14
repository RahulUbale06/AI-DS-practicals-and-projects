# 18. Write a Python Tkinter calculator application to perform
# addition, subtraction, multiplication, and division.
# Tkinter Calculator

import tkinter as tk
from tkinter import messagebox

# Function
def calculate(operation):

    try:

        num1 = float(entry1.get())

        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            result = num1 / num2

        messagebox.showinfo("Result", f"Result = {result}")

    except ZeroDivisionError:

        messagebox.showerror("Error", "Cannot divide by zero")

    except ValueError:

        messagebox.showerror("Error", "Invalid input")


# Window
root = tk.Tk()

root.title("Calculator")

root.geometry("300x250")

# Inputs
tk.Label(root, text="Enter First Number").pack()

entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()

entry2 = tk.Entry(root)
entry2.pack()

# Buttons
tk.Button(root, text="Add", command=lambda: calculate("+")).pack()

tk.Button(root, text="Subtract", command=lambda: calculate("-")).pack()

tk.Button(root, text="Multiply", command=lambda: calculate("*")).pack()

tk.Button(root, text="Divide", command=lambda: calculate("/")).pack()

root.mainloop()