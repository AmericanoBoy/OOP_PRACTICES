import lib
import pytest

def test_reverse_words_correct_input_data_exsist_result():
    a = 'маркс энгельс ленин сталин'
    expected = 'сталин ленин энгельс маркс'
    result = lib.reverse_words(a)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_reverse_words_correct_input_data_not_exsist_result():
    a = '   '
    expected = 'исходная строка пуста'
    result = lib.reverse_words(a)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_reverse_words_fatal_correct_input_data():
    a = 2
    with pytest.raises(TypeError):
        lib.count_occurrences(a)
    