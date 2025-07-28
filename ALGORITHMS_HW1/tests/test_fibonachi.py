
import pytest
from ALGORITHMS_HW1 import fibonachi

@pytest.mark.parametrize('number, expected',
                           [[0, [0]],
                            [1, [0,1]],
                            [5, [0,1,1,2,3]],
                            [11, [0,1,1,2,3,5,8,13,21,34,55]]
                            ])
def test_fibonachi_number_more_0_1_option(number, expected):
    res = fibonachi.create_fibonachi_array_1_option(number)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

@pytest.mark.parametrize('number, expected',
                           [[0, [0]],
                            [1, [0,1]],
                            [5, [0,1,1,2,3]],
                            [11, [0,1,1,2,3,5,8,13,21,34,55]]
                            ])
def test_fibonachi_number_more_0_2_option(number, expected):
    res = fibonachi.create_fibonachi_array_2_option(number)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_fibonachi_number_less_0_1_option():
    with pytest.raises(ValueError):
        fibonachi.create_fibonachi_array_1_option(-10)

def test_fibonachi_number_less_0_2_option():
    with pytest.raises(ValueError):
        fibonachi.create_fibonachi_array_2_option(-5)

def test_fibonachi_number_type_float_1_option():
    with pytest.raises(TypeError):
        fibonachi.create_fibonachi_array_1_option(5.5)

def test_fibonachi_number_type_float_2_option():
    with pytest.raises(TypeError):
        fibonachi.create_fibonachi_array_2_option(8.12345)

def test_fibonachi_number_type_str_1_option():
    with pytest.raises(TypeError):
        fibonachi.create_fibonachi_array_1_option('че ,вообще,')

def test_fibonachi_number_type_str_2_option():
    with pytest.raises(TypeError):
        fibonachi.create_fibonachi_array_2_option('происходит ?')



