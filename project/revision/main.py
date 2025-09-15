from function import is_number_bigger_then_given


def main():
    result = is_number_bigger_then_given(candidate_number=5)
    print(result)

    result = is_number_bigger_then_given(candidate_number=5, theshold=1)
    print(result)



if __name__ == "__main__":
    main()
