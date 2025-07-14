import lib
import pytest

def test_find_elem_correct_input_data_exsist_result():
    a = [4, 6, 3, 0, 8, 1]
    b = 3
    expected = 2
    result = lib.find_elem(a, b)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_find_elem_correct_input_data_not_exsist_result():
    a = [4, 6, 3, 0, 8, 1]
    b = 11
    expected = 'искомых элементов в списке нет'
    result = lib.find_elem(a, b)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_find_elem_uncorrect_input_data():
    a = 'eeeeeapp'
    b = 'a'
    with pytest.raises(ValueError):
        lib.count_occurrences(a, b)
    

def test_find_elem_fatal_uncorrect_input_data():
    a = 12
    b = 'e'
    with pytest.raises(ValueError):
        lib.count_occurrences(a, b)
