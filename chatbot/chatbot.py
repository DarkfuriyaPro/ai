import random


def chat() -> None:
    while True:
        command = input("Enter command: (hi/how are you/bye/exit: ")
        if command == "hi":
            print("Hello!")
        elif command == "how are you":
            answers = ["I'm fine.", "Great!", "Not bad"]
            print(random.choice(answers))
        elif command == "bye":
            print("Good bye!")
        elif command == "exit":
            break
        else:
            print("I didn't understand.")

chat()