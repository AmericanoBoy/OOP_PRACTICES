import lib
import pytest

def test_count_occurrences_correct_input_data_exsist_result():
    a = [4, 3, 3, 0, 8, 3]
    b = 3
    expected = 3
    result = lib.count_occurrences(a, b)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_count_occurrences_correct_input_data_not_exsist_result():
    a = [4, 6, 3, 0, 8, 1]
    b = 11
    expected = 0
    result = lib.count_occurrences(a, b)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_count_occurrences_uncorrect_input_data():
    a = 'eeeeeapp'
    b = 'a'
    with pytest.raises(ValueError):
        lib.count_occurrences(a, b)


def test_count_occurrences_fatal_uncorrect_input_data():
    a = 12
    b = []
    with pytest.raises(ValueError):
        lib.count_occurrences(a, b)