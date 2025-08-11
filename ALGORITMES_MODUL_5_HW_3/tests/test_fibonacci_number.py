
import pytest
from ALGORITMES_MODUL_5_HW_3 import fibonacci_number

@pytest.mark.parametrize('number, expected',
                           [[3, 2],
                            [10, 55],
                            [20, 6765],
                            [30, 832040]]
                         )
def test_fibonacci_number_all_date_true(number, expected):
    res = fibonacci_number.fibonacci_number(number)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_fibonacci_number_date_very_big():
    with pytest.raises(ValueError):
        fibonacci_number.fibonacci_number(1000000)


def test_fibonacci_number_date_not_type_int():
    with pytest.raises(TypeError):
        fibonacci_number.fibonacci_number('боб')

def test_fibonacci_number_date_type_int_but_less_1():
    with pytest.raises(ValueError):
        fibonacci_number.fibonacci_number(-2)