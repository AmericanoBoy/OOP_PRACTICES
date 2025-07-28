
import pytest
from ALGORITHMS_HW1 import factorial

@pytest.mark.parametrize('number, expected',
                           [[0, 1],
                            [1,1],
                            [10, 3628800],
                            [30,265252859812191058636308480000000]]
                         )
def test_factorial_if_number_more_0_high_speed(number, expected):
    res = factorial.factorial_of_number_high_search_speed(number)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

@pytest.mark.parametrize('number, expected',
                           [[0, 1],
                            [1,1],
                            [10, 3628800],
                            [30,265252859812191058636308480000000]]
                         )
def test_factorial_if_number_more_0_average_speed(number, expected):
    res = factorial.factorial_of_number_average_search_speed(number)
    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_factorial_if_number_less_0_high_speed():
    with pytest.raises(ValueError):
        factorial.factorial_of_number_high_search_speed(-1)

def test_factorial_if_number_less_0_average_speed():
    with pytest.raises(ValueError):
        factorial.factorial_of_number_average_search_speed(-5)

def test_factorial_if_number_less_0_low_speed():
    with pytest.raises(ValueError):
        factorial.factorial_of_number_low_search_speed(-5)

def test_factorial_if_number_is_not_type_int_high_speed():
    with pytest.raises(TypeError):
        factorial.factorial_of_number_high_search_speed(5.12345)

def test_factorial_if_number_is_not_type_int_average_speed():
    with pytest.raises(TypeError):
        factorial.factorial_of_number_average_search_speed(5.12345)

def test_factorial_if_number_is_not_type_int_low_speed():
    with pytest.raises(TypeError):
        factorial.factorial_of_number_low_search_speed(5.12345)

def test_factorial_if_number_more_20_and_low_speed_algorithm():
    with pytest.raises(ValueError):
        factorial.factorial_of_number_low_search_speed(25)

def test_factorial_if_number_is_type_str_high_speed():
    with pytest.raises(TypeError):
        factorial.factorial_of_number_high_search_speed('кто я')

def test_factorial_if_number_is_type_str_average_speed():
    with pytest.raises(TypeError):
        factorial.factorial_of_number_average_search_speed('что я')

def test_factorial_if_number_is_type_str_low_speed():
    with pytest.raises(TypeError):
        factorial.factorial_of_number_low_search_speed('где я')

