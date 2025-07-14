import lib
import pytest

def test_find_substr_correct_input_exsist_search():
    a = 'Учиться, учиться, учиться и еще раз учиться!!!'
    b = 'учиться'
    expected = 0
    result = lib.find_substr(a,b)
    assert result == expected, f'Ожидалось: {expected}, получено: {result}'

def test_find_substr_correct_input_not_exsist_search():
    a = 'Учиться, учиться, учиться и еще раз учиться!!!'
    b = 'электрификация'
    expected = 'Искомая подстрока не найдена'
    result = lib.find_substr(a,b)
    assert result == expected, f'Ожидалось: {expected}, получено: {result}'

def test_find_substr_correct_input_but_uncorrect_len():
    a = 'Капитализм'
    b = 'Капитализм беременен фашизмом'
    with pytest.raises(ValueError):
        lib.count_occurrences(a, b)
    

def test_find_substr_uncorrect_input():
    a=3
    b='абырвалг'
    with pytest.raises(ValueError):
        lib.count_occurrences(a, b)