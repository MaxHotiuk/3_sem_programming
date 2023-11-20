from worker_database import WorkerDatabase
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else: _ = system('clear')

def start_menu(menu):
    clear()
    for key in menu.keys():
        print(key)
    return input()

def __main__():
    worker_database = WorkerDatabase()
    menu = {
        "1: Read CSV": worker_database.read_csv,
        "2: Delete worker": worker_database.delete_worker_by_id,
        "3: Add worker": worker_database.add_worker,
        "4: Edit worker": worker_database.edit_by_id,
        "5: Print CSV": worker_database.print_csv,
        "6: Print workers": worker_database.print_workers,
        "7: Sort workers": worker_database.sort,
        "8: Search worker": worker_database.search,
        "9: Exit": exit
    }
    while True:
        n = start_menu(menu)
        for key in menu.keys():
            if n + ":" in key:
                menu[key]()
        input("Press Enter to continue...")

if __name__ == "__main__":
    __main__()