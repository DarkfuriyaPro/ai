age = int(input("How old are you?"))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("You are adult")
else:
    print("You are minor")