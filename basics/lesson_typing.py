def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> None:
    print("Hello", name)


def get_user_age(user: dict[str, int]) -> int:
    return user["age"]


def process(items: list[int]) -> list[str]:
    return [str(x) for x in items]

def process(items: list[int]) -> list[int]:
    return [x for x in items]