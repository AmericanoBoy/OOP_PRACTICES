
import pytest
from ALGORITMES_MODUL_5_HW_3 import reverse_string

@pytest.mark.parametrize('string, expected',
                           [['ров', 'вор'],
                            ['баобаб', 'бабоаб'],
                            ['ток', 'кот'],
                            ['кот ток', 'кот ток']]
                         )
def test_reverse_string_all_date_true(string, expected):
    res = reverse_string.reverse_string(string)
    assert expected == res, f'Ожидали: {expected} получили:{res}'

def test_reverse_string_date_very_long():
    with pytest.raises(ValueError):
        reverse_string.reverse_string('i' * 10000)

def test_reverse_string_date_not_string():
    with pytest.raises(TypeError):
        reverse_string.reverse_string(69)