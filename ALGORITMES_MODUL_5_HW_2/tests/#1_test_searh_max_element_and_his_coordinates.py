import pytest
from ALGORITMES_MODUL_5_HW_2 import search_max_element_and_his_coordinates


def test_search_max_element_and_his_coordinates_when_all_datas_correct():
    array,start,end = [1,3,2,5,4,7,0,1],2,6
    expected = [7,5,2]
    res = search_max_element_and_his_coordinates.max_in_range_between_start_and_end(array,start,end)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_search_max_element_and_his_coordinates_when_array_not_list():
    with pytest.raises(TypeError):
        search_max_element_and_his_coordinates.max_in_range_between_start_and_end('we',2,3)

def test_search_max_element_and_his_coordinates_when_len_array_is_0():
    with pytest.raises(ValueError):
        search_max_element_and_his_coordinates.max_in_range_between_start_and_end([],2,3)

def test_search_max_element_and_his_coordinates_when_uncorrect_diapasone_search():
    with pytest.raises(ValueError):
        search_max_element_and_his_coordinates.max_in_range_between_start_and_end([1,6,3,7],-2,12)

def test_search_max_element_and_his_coordinates_when_uncorrect_element_iteration():
    with pytest.raises(TypeError):
        search_max_element_and_his_coordinates.max_in_range_between_start_and_end(['w',1,5,'3',4,'eee'],2,5)



