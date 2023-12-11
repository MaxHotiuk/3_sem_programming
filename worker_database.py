from worker import Worker
import csv
from decorators import *
from validation import *
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import simpledialog

class WorkerDatabase:
    def __init__(self):
        self.workers = []
    
    def read_csv(self):
        filename = simpledialog.askstring("Input", "Enter the filename:")
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    worker = Worker(row['name'], row['surname'], row['department'], row['salary'])
                    if worker not in self.workers:
                        self.workers.append(worker)
                simpledialog.messagebox.showinfo("Success", "CSV file read successfully.")
        except FileNotFoundError:
            simpledialog.messagebox.showinfo("Failure", f"The file {filename} does not exist.")
        except csv.Error as e:
            simpledialog.messagebox.showinfo("Failure", f"An error occurred while reading the CSV file: {e}")

    def delete_worker_by_id(self):
        id = simpledialog.askstring("Input", "Enter worker's id: ")
        while not integer_validation(id):
            simpledialog.messagebox.showinfo("Failure", "Invalid id. Please enter a valid integer:")
            id = simpledialog.askstring("Input", "Enter worker's id: ")
        id = int(id)
        try:
            worker_to_delete = next(worker for worker in self.workers if worker.id == id)
            self.workers.remove(worker_to_delete)
        except StopIteration:
            simpledialog.messagebox.showinfo("Failure", "No worker found with the provided id.")

    def add_worker(self):
        name = simpledialog.askstring("Input", "Enter worker's name:")
        while not validate_name(name):
            simpledialog.messagebox.showinfo("Failure", "Invalid name. Please enter again:")
            name = simpledialog.askstring("Input", "Enter worker's name:")

        surname = simpledialog.askstring("Input", "Enter worker's surname:")
        while not validate_name(surname):
            simpledialog.messagebox.showinfo("Failure", "Invalid surname. Please enter again:")
            surname = simpledialog.askstring("Input", "Enter worker's surname:")

        department = simpledialog.askstring("Input", "Enter worker's department:")

        salary = simpledialog.askstring("Input", "Enter worker's salary:")
        while not numeric_validation(salary):
            simpledialog.messagebox.showinfo("Failure", "Invalid salary. Please enter a valid integer:")
            salary = simpledialog.askstring("Input", "Enter worker's salary:")

        worker = Worker(name, surname, department, int(salary))
        self.workers.append(worker)

    def edit_by_id(self):
        id = simpledialog.askstring("Input", "Enter worker's id: ")
        while not integer_validation(id):
            simpledialog.messagebox.showinfo("Failure", "Invalid id. Please enter a valid integer:")
            id = simpledialog.askstring("Input", "Enter worker's id: ")
        id = int(id)
        choice = simpledialog.askstring("Input", """
              What to edit?
              1. Name
              2. Surname
              3. Department
              4. Salary""")
        if choice == "1":
            name = simpledialog.askstring("Input", "Enter new name:")
            while not validate_name(name):
                simpledialog.messagebox.showinfo("Failure", "Invalid name. Please enter again:")
                name = simpledialog.askstring("Input", "Enter new name:")
            self.workers[id-1].name = name
        elif choice == "2":
            surname = simpledialog.askstring("Input", "Enter new surname:")
            while not validate_name(surname):
                simpledialog.messagebox.showinfo("Failure", "Invalid surname. Please enter again:")
                surname = simpledialog.askstring("Input", "Enter new surname:")
            self.workers[id-1].surname = surname
        elif choice == "3":
            department = simpledialog.askstring("Input", "Enter new department:")
            while not validate_name(department):
                simpledialog.messagebox.showinfo("Failure", "Invalid department. Please enter again:")
                department = simpledialog.askstring("Input", "Enter new department:")
            self.workers[id-1].department = department
        elif choice == "4":
            salary = simpledialog.askstring("Input", "Enter new salary:")
            while not integer_validation(salary):
                simpledialog.messagebox.showinfo("Failure", "Invalid salary. Please enter a valid integer:")
                salary = simpledialog.askstring("Input", "Enter new salary:")
            self.workers[id-1].salary = int(salary)
        else:
            simpledialog.messagebox.showinfo("Failure", "Wrong input!")

    @sort_decorator
    def sort(self, choice):
        if choice == "1":
            self.workers.sort(key=lambda x: x.name)
        elif choice == "2":
            self.workers.sort(key=lambda x: x.surname)
        elif choice == "3":
            self.workers.sort(key=lambda x: x.department)
        elif choice == "4":
            self.workers.sort(key=lambda x: x.salary)
        else:
            simpledialog.messagebox.showinfo("Failure", "Wrong input!")

    @search_decorator
    def search(self, choice, query):
        if choice == "1":
            for worker in self.workers:
                if worker.name == query:
                    return worker
        elif choice == "2":
            for worker in self.workers:
                if worker.surname == query:
                    return worker
        elif choice == "3":
            for worker in self.workers:
                if worker.department == query:
                    return worker
        elif choice == "4":
            for worker in self.workers:
                if worker.salary == int(query):
                    return worker
        else:
            simpledialog.messagebox.showinfo("Failure", "Wrong input!")    

    def print_csv(self):
        filename = simpledialog.askstring("Input", "Enter filename: ")
        try:
            with open(filename, "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["name", "surname", "department", "salary"])
                for worker in self.workers:
                    writer.writerow([worker.name, worker.surname, worker.department, str(worker.salary)])
        except FileNotFoundError:
            simpledialog.messagebox.showinfo("Failure", f"The file {filename} cannot be opened.")
        except csv.Error as e:
            simpledialog.messagebox.showinfo("Failure", f"An error occurred while writing to the CSV file: {e}")
            
    def sector_diagram(self):
        df = pd.DataFrame([worker.__dict__ for worker in self.workers])

        departments = df['department'].value_counts()

        plt.pie(departments.values, labels=departments.index, autopct='%1.1f%%')
        plt.show()

    def print_workers(self):
        output = ""
        for worker in self.workers:
            output += str(worker) + "\n"
        simpledialog.messagebox.showinfo("Workers", output)
            