import lib
import pytest

def test_is_palindrome_correct_input_data_exsist_result():
    a = 'шиш'
    expected = True
    result = lib.is_palindrome(a)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_is_palindrome_correct_input_data_not_exsist_result():
    a = 'шишка'
    expected = False
    result = lib.is_palindrome(a)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_is_palindrome_uncorrect_input_data():
    a = '  '
    expected = 'исходная строка пуста'
    result = lib.is_palindrome(a)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"