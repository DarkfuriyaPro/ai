count = 0

while True:
    command = input("Enter command: hi / bye / count")

    if command == "hi":
        print("Hi!")
        count += 1
    elif command == "count":
        print(f"You said hi {count} times")
    elif  command == "bye":
        print("Goodbye!")
        break
    else:
        print("Unknown command")