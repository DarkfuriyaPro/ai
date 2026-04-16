def greet(name):
    print(f"Hello {name}")

def age_info(age):
    return age

def can_vote(age):
    if age >= 18:
        print("Can vote")
    else:
        print("Cannot vote")


first_name = "Ann"
greet(first_name)

age = age_info(20)
print(f"You are {age} years old")
can_vote(age)