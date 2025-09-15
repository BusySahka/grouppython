from servises.logger import logger


def return_hello_buddy() -> str:
    result: str = "Hello, buddy"
    logger.info(f"return_hello_buddy -> {result}")
    return result


def return_biggest_num_from_array(arr: list) -> float:
    if not arr:
        logger.info("return_biggest_num_from_array: array is empty -> 0")
        return 0

    biggest_num: float = arr[0]

    for elem in arr:
        if isinstance(elem, (int, float)):
            if elem > biggest_num:
                biggest_num = elem

    logger.info(f"return_biggest_num_from_array({arr}) -> {biggest_num}")
    return biggest_num


def multiply_two_numbers(number_1: float, number_2: float) -> float:
    result: float = number_1 * number_2
    logger.info(f"multiply_two_numbers({number_1=}, {number_2=}) -> {result}")
    return result

