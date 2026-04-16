tasks = []

def add_task():
    task = input("Task: ")
    tasks.append(task)
    print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    show_tasks()
    index = int(input("Enter task number: "))
    tasks.pop(index - 1)
    print("Task deleted!")

while True:
    command = input("Command (add/show/delete/exit): ")

    if command == "add":
        add_task()

    elif command == "show":
        show_tasks()

    elif command == "delete":
        delete_task()

    elif command == "exit":
        break

    else:
        print("Unknown command")
