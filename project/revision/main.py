from function import is_number_bigger_then_given
from project.revision.function import add_salt_to_list
from hw_functions_utils import return_hello_buddy, return_biggest_num_from_array, multiply_two_numbers
from revision.utils import say_hello
from utils import greet_person, is_even, reverse_string, calculate_average, add_person_to_list, count_vowels, fahrenheit_to_celsius, say_hello

def main():
    #result = is_number_bigger_then_given(candidate_number=5)
    #print(result)
    #result = is_number_bigger_then_given(candidate_number=5, theshold=1)
    #print(result) #given_list = [] #add_salt_to_list(given_list) #add_salt_to_list(given_list) #print(given_list)
    #print(return_hello_buddy())
    #print(return_biggest_num_from_array([10, "a", 5.5, None, 22, 5, "d"]))
    #print(multiply_two_numbers(7, 9))
    print(greet_person("Олександра"))
    print(is_even(16))
    print(reverse_string("Привіт"))
    print(calculate_average([1, 2, 3, 4, 5]))
    print(add_person_to_list(["Олена", "Вікторія"], "Саша"))
    print(count_vowels("Як ти, друже?"))
    print(fahrenheit_to_celsius(1000))
    print(say_hello("Олександра"))


if __name__ == "__main__":
    main()
