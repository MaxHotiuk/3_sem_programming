class Worker:
    _id_generator = iter(range(1, 10**6))

    def __init__(self, name, surname, department, salary=0):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.department = department
        self.id = next(self._id_generator)
    
    def __str__(self):
        return f"{self.name} {self.surname}: {self.department}, {self.salary}"
    
    def set_id(self, id):
        self.__id = id

    def get_id(self):   
        return self.__id

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname
    
