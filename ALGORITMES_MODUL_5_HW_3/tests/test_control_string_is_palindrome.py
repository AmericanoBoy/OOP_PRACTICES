
import pytest
from ALGORITMES_MODUL_5_HW_3 import control_string_is_palindrome

@pytest.mark.parametrize('string, expected',
                           [['боб', True],
                            ['баобаб', False],
                            ['боб боб', True],
                            ['баобаб баобаб', False]]
                         )
def test_control_string_is_palindrome_all_date_true(string, expected):
    res = control_string_is_palindrome.control_string_is_palindrome(string)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_control_string_is_palindrome_date_very_long():
    with pytest.raises(ValueError):
        control_string_is_palindrome.control_string_is_palindrome('i' * 10000)


def test_control_string_is_palindrome_date_not_string():
    with pytest.raises(TypeError):
        control_string_is_palindrome.control_string_is_palindrome(69)