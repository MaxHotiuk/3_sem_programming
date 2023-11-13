from worker import Worker
import csv

def sort_decorator(func):
    def wrapper(self):
        print("Sort by: ")
        print("1. Name")
        print("2. Surname")
        print("3. Department")
        print("4. Salary")
        choice = input()
        func(self, choice)
        print("Sorted by ")
        if choice == "1":
            print("name")
        elif choice == "2":
            print("surname")
        elif choice == "3":
            print("department")
        elif choice == "4":
            print("salary")
    return wrapper

def search_decorator(func):
    def wrapper(self):
        print("Search by: ")
        print("1. Name")
        print("2. Surname")
        print("3. Department")
        print("4. Salary")
        choice = input()
        print("Enter search query: ")
        query = input()
        print("Result is: ")
        print(func(self, choice, query))
    return wrapper

class WorkerDatabase:
    def __init__(self):
        self.workers = []
    
    def read_csv(self):
        filename = input("Enter filename: ")
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            id = 1
            for row in reader:
                if (len(self.workers) != 0):
                    if (self.workers[-1].get_id() > id):
                        id = self.workers[-1].get_id() + 1
                self.workers.append(Worker(row['name'], row['surname'], row['department'], row['salary']))
                self.workers[-1].set_id(id)
                id += 1
    
    def delete_worker_by_id(self):
        id = input("Enter worker's id: ")
        self.workers.pop(id-1)

    def add_worker(self):
        print("Enter worker's name:")
        name = input()
        print("Enter worker's surname:")
        surname = input()
        print("Enter worker's department:")
        department = input()
        print("Enter worker's salary:")
        salary = input()
        if (len(self.workers) != 0):
            id = self.workers[-1].get_id() + 1
        else:
            id = 1
        worker = Worker(name, surname, department, salary)
        self.workers.append(worker)

    def edit_by_id(self):
        id = int(input("Enter worker's id: "))
        print("What to edit?")
        print("1. Name")
        print("2. Surname")
        print("3. Department")
        print("4. Salary")
        choice = input()
        if choice == "1":
            print("Enter new name:")
            name = input()
            self.workers[id-1].name = name
        elif choice == "2":
            print("Enter new surname:")
            surname = input()
            self.workers[id-1].surname = surname
        elif choice == "3":
            print("Enter new department:")
            department = input()
            self.workers[id-1].department = department
        elif choice == "4":
            print("Enter new salary:")
            salary = input()
            self.workers[id-1].salary = salary
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
                if str(worker.salary) == query:
                    return worker
        else:
            print("Wrong input!")    

    def print_csv(self):
        filename = input("Enter filename: ")
        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["name", "surname", "department", "salary"])
            for worker in self.workers:
                writer.writerow([worker.name, worker.surname, worker.department, str(worker.salary)])

    def print_workers(self):
        for worker in self.workers:
            print(worker)
            