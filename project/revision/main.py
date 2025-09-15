from function import is_number_bigger_then_given
from project.revision.function import add_salt_to_list
from hw_functions_utils import return_hello_buddy, return_biggest_num_from_array, multiply_two_numbers

def main():
    #result = is_number_bigger_then_given(candidate_number=5)
    #print(result)
    #result = is_number_bigger_then_given(candidate_number=5, theshold=1)
    #print(result)
    #given_list = []
    #add_salt_to_list(given_list)
    #add_salt_to_list(given_list)
    #print(given_list)
    print(return_hello_buddy())
    print(return_biggest_num_from_array([10, "a", 5.5, None, 22, 5, "d"]))
    print(multiply_two_numbers(7, 9))



if __name__ == "__main__":
    main()
