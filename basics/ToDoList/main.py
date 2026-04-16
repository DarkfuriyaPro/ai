from logic import add_task, delete_task, show_tasks
from storage import save_tasks, load_tasks

tasks = load_tasks()

def add():
    task = input("Task: ")
    add_task(task)
    save_tasks(show_tasks())

def delete():
    index = int(input("Number: "))
    delete_task(index - 1)
    save_tasks(show_tasks())

def show():
    tasks = show_tasks()

    if not tasks:
        print("No tasks")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


while True:
    command = input("add/show/delete/exit: ")

    if command == "add":
        add()

    elif command == "show":
        show()

    elif command == "delete":
        delete()

    elif command == "exit":
        break

    else:
        print("Unknown command")