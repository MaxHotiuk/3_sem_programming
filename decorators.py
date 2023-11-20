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