import sys
from Converter.converter import convert


def main() -> None:
    if len(sys.argv) != 4:
        print("Использование: python main.py USD EUR 100")
        return

    from_currency: str = sys.argv[1].upper()
    to_currency: str = sys.argv[2].upper()

    try:
        amount: float = float(sys.argv[3])
    except ValueError:
        print("Сумма должна быть числом")
        return

    try:
        result: float = convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()