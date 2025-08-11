
import pytest
from ALGORITMES_MODUL_5_HW_3 import sum_even_elements_lst

@pytest.mark.parametrize('array, expected',
                           [[[3,2,1,4], 6],
                            [[1,1,1], 0],
                            [[100,3,311,100], 200],
                            [[34.0,30.0,23.0], 64.0]]
                         )
def test_sum_even_element_lst_all_date_true(array, expected):
    res = sum_even_elements_lst.sum_even_elements_lst(array)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_sum_even_element_lst_date_very_big():
    with pytest.raises(ValueError):
        sum_even_elements_lst.sum_even_elements_lst([i for i in range(2000000)])

def test_sum_even_element_lst_iteration_date_not_type_int():
    with pytest.raises(TypeError):
        sum_even_elements_lst.sum_even_elements_lst([2,3,'eee',5])

def test_sum_even_element_lst_date_not_type_int():
    with pytest.raises(TypeError):
        sum_even_elements_lst.sum_even_elements_lst('боб')