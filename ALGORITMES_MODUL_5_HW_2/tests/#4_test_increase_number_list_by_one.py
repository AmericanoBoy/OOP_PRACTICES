
import pytest
from ALGORITMES_MODUL_5_HW_2 import increase_number_list_by_one

@pytest.mark.parametrize('array, expected',
                           [[[1,0,9],[1,1,0]],
                            [[9,9,9],[1,0,0,0]],
                            [[3,4,5,6], [3,4,5,7]],
                            [[1,9,9],[2,0,0]]]
                         )
def test_increase_number_list_by_one_all_correct_data(array, expected):
    res = increase_number_list_by_one.increase_number_list_by_one(array)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_increase_number_list_by_one_when_array_is_not_list():
    with pytest.raises(TypeError):
        increase_number_list_by_one.increase_number_list_by_one('trpr')

def test_increase_number_list_by_one_when_len_array_is_0():
    with pytest.raises(ValueError):
        increase_number_list_by_one.increase_number_list_by_one([])

def test_increase_number_list_by_one_when_iteration_element_is_not_int():
    with pytest.raises(TypeError):
        increase_number_list_by_one.increase_number_list_by_one(['w',3,'334',5,6])


