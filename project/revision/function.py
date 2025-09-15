from uuid import uuid4

def is_number_bigger_then_given(candidate_number: float, theshold: float = 10) -> bool:
    """acording to the task #745736"""
    return candidate_number > theshold


def add_salt_to_list(given_list: list) -> None:
    """WARNING"""
    id = uuid4().hex
    print(id)
    given_list.append(id)