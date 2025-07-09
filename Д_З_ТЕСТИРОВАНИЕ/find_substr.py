import lib_1

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
    expected = 'Длина искомой подстроки не может быть больше длины строки'
    result = lib.find_substr(a, b)
    assert result == expected, f'Ожидалось: {expected}, получено: {result}'

def test_find_substr_uncorrect_input():
    a=3
    b='абрвалг'
    expected = 'Неверный тип данных для поиска'
    result = lib.find_substr(a, b)
    assert result == expected, f'Ожидалось: {expected}, получено: {result}'