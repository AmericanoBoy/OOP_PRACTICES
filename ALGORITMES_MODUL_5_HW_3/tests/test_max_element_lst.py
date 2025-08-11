
import pytest
from ALGORITMES_MODUL_5_HW_3 import max_element_lst

@pytest.mark.parametrize('array, expected',
                           [[[3,2,1], 3],
                            [[10,23,112,4,45], 112],
                            [[1,2,20,1234], 1234],
                            [[34,30,23], 34]]
                         )
def test_max_element_lst_all_date_true(array, expected):
    res = max_element_lst.max_element_lst(array)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_max_element_lst_date_very_big():
    with pytest.raises(ValueError):
        max_element_lst.max_element_lst([i for i in range(2000000)])


def test_max_element_lst_date_not_type_int():
    with pytest.raises(TypeError):
        max_element_lst.max_element_lst('боб')