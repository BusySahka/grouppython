from revision.function import is_number_bigger_then_given, get_string_length_with_no_whitespaces, get_auto_distance

def test_is_number_bigger_then_given_1():
    given_number = 5
    result = is_number_bigger_then_given(given_number)
    expected_result = False
    assert result == expected_result


def test_1():
    pass


def test_get_string_length_with_no_whitespaces():
    given_string = ""
    expected_result = 0
    actual_result = get_string_length_with_no_whitespaces(given_string)
    assert actual_result == expected_result


def test_get_auto_distance():
    given_speed = 10
    given_time = 6
    actual_result = get_auto_distance(speed=given_speed, time=given_time)
    expectet_result = 60
    assert actual_result == expectet_result
