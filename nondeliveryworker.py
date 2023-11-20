from worker import Worker

class NonDeliveryWorker(Worker):
    def __init__(self, name, surname, department, salary):
        super().__init__(name, surname, department, salary)