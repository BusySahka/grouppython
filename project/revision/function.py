from uuid import uuid4

def is_number_bigger_then_given(candidate_number: float, theshold: float = 10) -> bool:
    """acording to the task #745736"""
    return candidate_number > theshold


def add_salt_to_list(given_list: list) -> None:
    """WARNING"""
    id = uuid4().hex
    print(id)
    given_list.append(id)


def get_string_length_with_no_whitespaces(string: str) -> int:
    string_no_whitespaces = string.replace(" ", "")
    return len(string_no_whitespaces)

def get_auto_distance(speed: float, time: float) -> float:
    dictance =  speed * time
    return dictance