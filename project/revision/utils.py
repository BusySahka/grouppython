def greet_person(name: str = "Гість") -> str:
    return f"Привіт, {name}!"


def is_even(number: int) -> bool:
    return number % 2 == 0


def reverse_string(text: str) -> str:
    return text[::-1]


def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0


def add_person_to_list(people: list[str], person: str) -> list[str]:
    return people + [person]


def count_vowels(text: str,) -> int:
    vowels = "aeiouyаеєиіїоуюяAEIOUYАЕЄИІЇОУЮЯ"
    count = 0
    for character in text:
        if character in vowels:
            count += 1
    return count


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9

def say_hello(name: str) -> str:
    return f"Hello. {name}!"