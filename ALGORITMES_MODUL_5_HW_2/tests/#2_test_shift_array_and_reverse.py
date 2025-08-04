
import pytest
from ALGORITMES_MODUL_5_HW_2 import shift_array_and_reverse

#тестирование функции сдвига вправо и инверсии

def test_shift_array_right_and_reverse_all_correct_data():
    array = [1,2,3,4,5,6,7,8]
    shift_flag = 3
    expected = [5,4,3,2,1,8,7,6]
    res = shift_array_and_reverse.shift_array_right_and_reverse(array, shift_flag)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_shift_array_right_and_reverse_when_array_is_not_list():
    with pytest.raises(TypeError):
        shift_array_and_reverse.shift_array_right_and_reverse('trprprtr', 2)

def test_shift_array_right_and_reverse_when_len_array_is_0():
    with pytest.raises(ValueError):
        shift_array_and_reverse.shift_array_right_and_reverse([], 2)

def test_shift_array_right_and_reverse_when_shift_flag_more_len_array():
    with pytest.raises(ValueError):
        shift_array_and_reverse.shift_array_right_and_reverse([1,2,3,4,5,6,7], 8)

def test_shift_array_right_and_reverse_when_shift_flag_less_0():
    with pytest.raises(ValueError):
        shift_array_and_reverse.shift_array_right_and_reverse([1,2,3,4,5,6,7], -1)

#тестирование функции сдвига влево и инверсии

def test_shift_array_left_and_reverse_all_correct_data():
    array = [1,2,3,4,5,6,7,8]
    shift_flag = 3
    expected = [3,2,1,8,7,6,5,4]
    res = shift_array_and_reverse.shift_array_left_and_reverse(array, shift_flag)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_shift_array_left_and_reverse_when_array_is_not_list():
    with pytest.raises(TypeError):
        shift_array_and_reverse.shift_array_left_and_reverse('trprprtr', 2)

def test_shift_array_left_and_reverse_when_len_array_is_0():
    with pytest.raises(ValueError):
        shift_array_and_reverse.shift_array_left_and_reverse([], 2)

def test_shift_array_left_and_reverse_when_shift_flag_more_len_array():
    with pytest.raises(ValueError):
        shift_array_and_reverse.shift_array_left_and_reverse([1,2,3,4,5,6,7], 8)

def test_shift_array_left_and_reverse_when_shift_flag_less_0():
    with pytest.raises(ValueError):
        shift_array_and_reverse.shift_array_left_and_reverse([1,2,3,4,5,6,7], -1)

