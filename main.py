from worker_database import WorkerDatabase
from unit_tests import TestWorkerDatabase
import tkinter as tk
from tkinter import simpledialog

class GUI:
    def __init__(self, worker_database, tests):
        self.worker_database = worker_database
        self.tests = tests
        self.root = tk.Tk()
        self.create_buttons()
        self.output_label = tk.Label(self.root)
        self.output_label.pack()
        self.root.mainloop()
        

    def create_buttons(self):
        buttons = {
            "Read CSV": self.worker_database.read_csv,
            "Delete worker": self.worker_database.delete_worker_by_id,
            "Add worker": self.worker_database.add_worker,
            "Edit worker": self.worker_database.edit_by_id,
            "Print CSV": self.worker_database.print_csv,
            "Print workers": self.worker_database.print_workers,
            "Sort workers": self.worker_database.sort,
            "Search worker": self.worker_database.search,
            "Unit tests": self.tests.run_tests,
            "Diagram": self.worker_database.sector_diagram,
            "Exit": exit
        }

        for key in buttons.keys():
            button = tk.Button(self.root, text=key, command=buttons[key])
            button.pack()


def __main__():
    worker_database = WorkerDatabase()
    tests = TestWorkerDatabase()
    GUI(worker_database, tests)

if __name__ == "__main__":
    __main__()
