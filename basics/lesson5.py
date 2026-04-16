tasks = []

# загрузка из файла
try:
    file = open("tasks.txt", "r")
    tasks = file.read().splitlines()
    file.close()
except FileNotFoundError:
    tasks = []

while True:
    command = input("Enter command (add/show/exit): ")

    if command == "add":
        task = input("Task: ")
        tasks.append(task)

        file = open("tasks.txt", "w")
        for t in tasks:
            file.write(t + "\n")
        file.close()

    elif command == "show":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

    elif command == "exit":
        break

    else:
        print("Unknown command")