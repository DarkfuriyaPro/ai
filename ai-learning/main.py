
#Print name, age
name = input("What is your name?")
age = int(input("How old are you?"))
print(f"My name is {name}, i'm {age} years old.")

if age >= 18:
    print("Access is allowed")
else:
    print("Access is denied")

while True:
    mood = input("How do you feel?")
    if mood == "exit":
        break
    if mood == "good":
        print("Great!")
    elif mood == "bad":
        print("Hang in there!")
    else:
        print("Interesting!")
    


#Loops
numbers = [1,2,3,4,5,6]
for i in numbers:
    print(i)

for i in range(6):
    print(i)

#Ask 3 names
for i in range(3):
    name = input("What is your name?")
    if not name:
        print("Unvalid name.")
    else:
        print(f"Hello {name}")



#Functions
def ask_name() -> str:
    name = input("What is your name?")
    if not name:
        return "Unvalid name"
    else:
        return name
    
ask_name() 


#Mini AI
def ai_greeting() -> str:
    greet = input()
    if greet == "Hello":
        return  "Hello"
    else:
        return "I didn't understand"
