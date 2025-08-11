
import pytest
from ALGORITMES_MODUL_5_HW_3 import sum_all_elements_lst

@pytest.mark.parametrize('array, expected',
                           [[[3,2,1], 6],
                            [[1,4,6], 11],
                            [[100.2,200.1,300.4], 600.8],
                            [[-1,-2,-3], -1]]
                         )
def test_sum_all_element_lst_all_date_true(array, expected):
    res = sum_all_elements_lst.sum_all_elements_lst(array)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_sum_all_element_lst_date_very_big():
    with pytest.raises(ValueError):
        sum_all_elements_lst.sum_all_elements_lst([i for i in range(2000000)])


def test_sum_all_element_lst_date_not_type_int():
    with pytest.raises(TypeError):
        sum_all_elements_lst.sum_all_elements_lst('боб')

def test_sum_all_element_lst_iteration_date_not_type_int():
    with pytest.raises(TypeError):
        sum_all_elements_lst.sum_all_elements_lst([6,'oo',9,'eee'])
