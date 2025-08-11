
import pytest
from ALGORITMES_MODUL_5_HW_3 import sum_digits_number

@pytest.mark.parametrize('number, expected',
                           [[222,6],
                            [203,5],
                            [20708, 17],
                            [24501, 12]]
                         )
def test_sum_digits_number_all_date_true(number, expected):
    res = sum_digits_number.sum_digits_number(number)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_reverse_string_date_very_long():
    with pytest.raises(ValueError):
        sum_digits_number.sum_digits_number(int('2' * 20000))

def test_reverse_string_date_not_string():
    with pytest.raises(TypeError):
        sum_digits_number.sum_digits_number('боб')