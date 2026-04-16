def load_tasks():
    try:
        file = open("tasks.txt", "r")
        tasks = file.read().splitlines()
        file.close()
        return tasks
    except FileNotFoundError:
        return []

def save_tasks():
    file = open("tasks.txt", "w")

    for task in tasks:
        file.write(task + "\n")

    file.close()

def add_task():
    task = input("Task: ")
    tasks.append(task)
    save_tasks()
    print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    show_tasks()
    index = int(input("Number: "))
    tasks.pop(index - 1)
    save_tasks()
    print("Deleted!")

tasks = load_tasks()

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