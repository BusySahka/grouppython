def return_as_dictionary(func):
    def return_result_as_dict(*args, **kwargs):
        result = func(*args, **kwargs)
        return {"result": result}
    return return_result_as_dict


@return_as_dictionary
def calculate_sum(number_1, number_2):
    return number_1 + number_2

@return_as_dictionary
def greet_person(name):
    return f"Hello, {name}!"

@return_as_dictionary
def multiply_numbers(number1, number2, number3):
    return number1 * number2 * number3



