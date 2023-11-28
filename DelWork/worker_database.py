from worker import Worker
import csv
from decorators import *
from validation import *

class WorkerDatabase:
    def __init__(self):
        self.workers = []
    
    def read_csv(self):
        filename = input("Enter filename: ")
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    worker = Worker(row['name'], row['surname'], row['department'], row['salary'])
                    if worker not in self.workers:
                        self.workers.append(worker)
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
        except csv.Error as e:
            print(f"An error occurred while reading the CSV file: {e}")

    def delete_worker_by_id(self):
        id = input("Enter worker's id: ")
        while not integer_validation(id):
            print("Invalid id. Please enter a valid integer:")
            id = input()
        id = int(id)
        try:
            worker_to_delete = next(worker for worker in self.workers if worker.id == id)
            self.workers.remove(worker_to_delete)
        except StopIteration:
            print("No worker found with the provided id.")

    def add_worker(self):
        name = input("Enter worker's name:")
        while not validate_name(name):
            print("Invalid name. Please enter again:")
            name = input()

        surname = input("Enter worker's surname:")
        while not validate_name(surname):
            print("Invalid surname. Please enter again:")
            surname = input()

        department = input("Enter worker's department:")

        salary = input("Enter worker's salary:")
        while not numeric_validation(salary):
            print("Invalid salary. Please enter a valid integer:")
            salary = input()

        worker = Worker(name, surname, department, int(salary))
        self.workers.append(worker)

    def edit_by_id(self):
        id = input("Enter worker's id: ")
        while not integer_validation(id):
            print("Invalid id. Please enter a valid integer:")
            id = input()
        id = int(id)
        print("What to edit?")
        print("1. Name")
        print("2. Surname")
        print("3. Department")
        print("4. Salary")
        choice = input()
        if choice == "1":
            name = input("Enter new name:")
            while not validate_name(name):
                print("Invalid name. Please enter again:")
                name = input()
            self.workers[id-1].name = name
        elif choice == "2":
            surname = input("Enter new surname:")
            while not validate_name(surname):
                print("Invalid surname. Please enter again:")
                surname = input()
            self.workers[id-1].surname = surname
        elif choice == "3":
            department = input("Enter new department:")
            while not validate_name(department):
                print("Invalid department. Please enter again:")
                department = input()
            self.workers[id-1].department = department
        elif choice == "4":
            salary = input("Enter new salary:")
            while not integer_validation(salary):
                print("Invalid salary. Please enter a valid integer:")
                salary = input()
            self.workers[id-1].salary = int(salary)
        else:
            print("Wrong input!")

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
            print("Wrong input!")

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
            print("Wrong input!")    

    def print_csv(self):
        filename = input("Enter filename: ")
        try:
            with open(filename, "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["name", "surname", "department", "salary"])
                for worker in self.workers:
                    writer.writerow([worker.name, worker.surname, worker.department, str(worker.salary)])
        except FileNotFoundError:
            print(f"The file {filename} cannot be opened.")
        except csv.Error as e:
            print(f"An error occurred while writing to the CSV file: {e}")

    def print_workers(self):
        for worker in self.workers:
            print(worker)
            