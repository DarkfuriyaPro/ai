from typing import List

name = "Ann"
age = 24
city = "Moscow"

print(f"My name is {name}.")
print(f"I'm {age} years old.")
print(f"I live in {city}.")


def multiply(a: int, b: int) -> int:
    return a * b

def get_full_name(first_name: str, last_name: str) -> str:
    return first_name + " " + last_name

def print_items(items: List[str]) -> None:
    for item in items:
        print(item)