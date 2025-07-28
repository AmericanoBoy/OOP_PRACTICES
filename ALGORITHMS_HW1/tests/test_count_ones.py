
import pytest
from ALGORITHMS_HW1 import count_ones

@pytest.mark.parametrize('number, expected',
                           [[0, 0],
                            [1, 1],
                            [13, 3],
                            [1234, 5]]
                         )
def test_count_ones_number_more_0(number, expected):
    res = count_ones.count_ones_in_bin_number(number)
    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_count_ones_number_less_0():
    with pytest.raises(ValueError):
        count_ones.count_ones_in_bin_number(-5)


def test_count_ones_number_not_type_int():
    with pytest.raises(TypeError):
        count_ones.count_ones_in_bin_number('однако....')
