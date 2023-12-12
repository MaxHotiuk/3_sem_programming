from unittest import *
from worker_database import WorkerDatabase
import tkinter as tk
from tkinter import simpledialog

class TestWorkerDatabase(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        data = WorkerDatabase()
        self.worker_database = data

    def test_read_csv(self):
        simpledialog.messagebox.showinfo("Test", "Testing read_csv...")
        self.assertEqual(len(self.worker_database.workers), 3)

    def test_delete_worker_by_id(self):
        simpledialog.messagebox.showinfo("Test", "Testing delete_worker_by_id...")
        self.worker_database.delete_worker_by_id()
        self.assertEqual(len(self.worker_database.workers), 2)

    def test_add_worker(self):
        simpledialog.messagebox.showinfo("Test", "Testing add_worker...")
        self.worker_database.add_worker()
        self.assertEqual(len(self.worker_database.workers), 3)

    def test_print_csv(self):
        simpledialog.messagebox.showinfo("Test", "Testing print_csv...")
        self.worker_database.print_csv()

    def test_print_workers(self):
        simpledialog.messagebox.showinfo("Test", "Testing print_workers...")
        self.worker_database.print_workers()
        
    def test_sort_by_name(self):
        simpledialog.messagebox.showinfo("Test", "Testing sorting by NAME...")
        self.worker_database.sort()
        self.assertEqual(self.worker_database.workers[0].name, "Anatoly")
    
    def test_search(self):
        simpledialog.messagebox.showinfo("Test", "Testing search...")
        self.worker_database.search()
    
    def run_tests(self):
        simpledialog.messagebox.showinfo("Test", "Unit tests:")
        self.worker_database.read_csv()
        self.test_read_csv()
        self.test_delete_worker_by_id()
        self.test_add_worker()
        self.test_print_csv()
        self.test_print_workers()
        self.test_sort_by_name()
        self.test_search()
        simpledialog.messagebox.showinfo("Test", "All tests passed!")