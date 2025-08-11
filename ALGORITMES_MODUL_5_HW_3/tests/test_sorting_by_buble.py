
import pytest
from ALGORITMES_MODUL_5_HW_3 import sorting_by_buble

def test_sort_buble_all_dates_true():
    array = [-100,-200,-300]
    expected = [-300,-200,-100]
    res = sorting_by_buble.sort_buble(array)
    assert expected == res, f'Ожидали: {expected} получили:{res}'


def test_sort_buble_data_not_list():
    with pytest.raises(TypeError):
        sorting_by_buble.sort_buble(-5)


def test_sort_buble_iteration_element_not_int_or_float():
    with pytest.raises(TypeError):
        sorting_by_buble.sort_buble([1,'боб',3,2,'баобаб'])