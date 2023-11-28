from unittest import *
from worker_database import WorkerDatabase

class TestWorkerDatabase(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        data = WorkerDatabase()
        self.worker_database = data

    def test_read_csv(self):
        print("Testing read_csv...")
        self.assertEqual(len(self.worker_database.workers), 3)

    def test_delete_worker_by_id(self):
        print("Testing delete_worker_by_id...")
        self.worker_database.delete_worker_by_id()
        self.assertEqual(len(self.worker_database.workers), 2)

    def test_add_worker(self):
        print("Testing add_worker...")
        self.worker_database.add_worker()
        self.assertEqual(len(self.worker_database.workers), 3)

    def test_print_csv(self):
        print("Testing print_csv...")
        self.worker_database.print_csv()

    def test_print_workers(self):
        print("Testing print_workers...")
        self.worker_database.print_workers()
        
    def test_sort_by_name(self):
        print("Testing sorting by NAME...")
        self.worker_database.sort()
        self.assertEqual(self.worker_database.workers[0].name, "Boba")
    
    def test_search(self):
        print("Testing search...")
        self.worker_database.search()
    
    def run_tests(self):
        print("Unit tests:")
        self.worker_database.read_csv()
        self.test_read_csv()
        self.test_delete_worker_by_id()
        self.test_add_worker()
        self.test_print_csv()
        self.test_print_workers()
        self.test_sort_by_name()
        self.test_search()
        print("All tests passed!")