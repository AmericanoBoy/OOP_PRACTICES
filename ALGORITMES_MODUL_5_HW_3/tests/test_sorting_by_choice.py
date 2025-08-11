
import pytest
from ALGORITMES_MODUL_5_HW_3 import sorting_by_choice

def test_sorting_by_choice_all_dates_true():
    array = [1,4,6,-1,3.5,0]
    expected = f'Oтсорт. список: [-1, 0, 1, 3.5, 4, 6]\n'\
               f'Список поэтапно переставляемых эл_ов: [[-1, 1], [0, 4], [1, 6], [3.5, 6], [4, 6]]\n'\
               f'Произведено 5  этапов cравнений и обмена элементов списка.'
    res = sorting_by_choice.sort_choice(array)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_sorting_by_choice_data_not_list():
    with pytest.raises(TypeError):
        sorting_by_choice.sort_choice('баобаб')


def test_sorting_by_choice_iterations_data_not_int_or_float():
    with pytest.raises(TypeError):
        sorting_by_choice.sort_choice([1,2,7,6,'боб',3,8,'баобаб'])