import tkinter as tk
from tkinter import simpledialog

def sort_decorator(func):
    def wrapper(self):
        choice = simpledialog.askstring("Input", """
              Sort by:
              1. Name
              2. Surname
              3. Department
              4. Salary""")
        func(self, choice)
        output = "Sorted by "
        if choice == "1":
            output += "name"
        elif choice == "2":
            output += "surname"
        elif choice == "3":
            output += "department"
        elif choice == "4":
            output += "salary"
        simpledialog.messagebox.showinfo("Success", output)
    return wrapper

def search_decorator(func):
    def wrapper(self):
        choice = simpledialog.askstring("Input", """
              Search by:
              1. Name
              2. Surname
              3. Department
              4. Salary""")
        query = simpledialog.askstring("Input", "Enter search query: ")
        simpledialog.messagebox.showinfo("Success", "Result is: " + str(func(self, choice, query)))
    return wrapper