from function import is_number_bigger_then_given
from project.revision.function import add_salt_to_list


def main():
    result = is_number_bigger_then_given(candidate_number=5)
    print(result)

    result = is_number_bigger_then_given(candidate_number=5, theshold=1)
    print(result)

    add_salt_to_list([])



if __name__ == "__main__":
    main()
