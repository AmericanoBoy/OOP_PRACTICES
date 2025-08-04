import pytest
from ALGORITMES_MODUL_5_HW_2 import reverse_only_even_numbers_array

def test_reverse_only_even_numbers_array_all_correct_data():
    array = [1,2,3,4,5,6]
    expected = [1,6,3,4,5,2]
    res = reverse_only_even_numbers_array.reverse_only_even_numbers_array(array)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_reverse_only_even_numbers_array_when_array_is_not_list():
    with pytest.raises(TypeError):
        reverse_only_even_numbers_array.reverse_only_even_numbers_array('trpr')

def test_reverse_only_even_numbers_array_when_len_array_is_0():
    with pytest.raises(ValueError):
        reverse_only_even_numbers_array.reverse_only_even_numbers_array([])

def test_reverse_only_even_numbers_array_when_uncorrect_element_iteration():
    with pytest.raises(TypeError):
        reverse_only_even_numbers_array.reverse_only_even_numbers_array(['2','e',2,1,'p',4])