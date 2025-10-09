from typing import Callable
from functools import wraps


#Це головна функція-декоратор із параметром ndigits
def round_result(ndigits: int):
    """
    Декоратор, який автоматично округлює результат функції
    до заданої кількості знаків після коми.
    """

    # Це власне декоратор, який приймає функцію
    def decorator(func: Callable):
        # Використовуємо wraps, щоб не загубити ім’я і докстрінг функції
        @wraps(func)
        def inner(*args, **kwargs):
            """
            Внутрішня функція (іннер), яка викликає оригінальну функцію
            і округлює її результат, якщо це число.
            """

            # Викликаємо декоровану функцію
            result = func(*args, **kwargs)

            # Якщо результат — число, округлюємо його
            if isinstance(result, (int, float)):
                return round(result, ndigits)

            # Якщо результат не число — повертаємо без змін
            return result

        # Повертаємо внутрішню функцію
        return inner

    # Повертаємо сам декоратор
    return decorator



@round_result(2)  # округлення до 2 знаків після коми
def divide_numbers(number1: float, number2: float) -> float:
    """Функція для ділення двох чисел."""
    return number1 / number2


@round_result(3)  # округлення до 3 знаків після коми
def multiply_numbers(number_1: float, number_2: float) -> float:
    """Функція для множення двох чисел."""
    return number_1 * number_2


# Перевірка коду
print(divide_numbers(55, 3))     # Буде 18,33
print(multiply_numbers(8.675, 3.295))  # Буде 28,584
#Я використала log_decorator з урока та трошки видозмінила його