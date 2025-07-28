
import pytest
from ALGORITHMS_HW1 import palindrome

@pytest.mark.parametrize('number, expected',
                           [[000000, True],
                            [12, False],
                            [12321, True],
                            [0, True],
                            [1234567, False],
                            [87544578, True],
                            [1234322, False],
                            [89899898, True]]
                            )

def test_palindrome_value_number(number, expected):
    res = palindrome.calculating_palindrome(number)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_palindrome_not_value_number_more_0():
    with pytest.raises(ValueError):
        palindrome.calculating_palindrome(96785434567890888854)

def test_palindrome_not_value_number_less_0():
    with pytest.raises(ValueError):
        palindrome.calculating_palindrome(-9887666666666666666)

def test_palindrome_not_value_number_is_type_str():
    with pytest.raises(TypeError):
        palindrome.calculating_palindrome('елки-палки(((')

def test_palindrome_not_value_number_is_type_float():
    with pytest.raises(TypeError):
        palindrome.calculating_palindrome(1.2345)
