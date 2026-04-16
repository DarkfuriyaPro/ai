from typing import Dict
from Converter.rates import RATES


def convert(amount: float, from_currency: str, to_currency: str) -> float:
    rates: Dict[str, float] = RATES

    if from_currency not in rates:
        raise ValueError("Неизвестная валюта: " + from_currency)

    if to_currency not in rates:
        raise ValueError("Неизвестная валюта: " + to_currency)

    usd: float = amount / rates[from_currency]
    result: float = usd * rates[to_currency]

    return result