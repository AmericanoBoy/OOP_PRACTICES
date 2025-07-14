def find_substr(text: str, pattern: str):
    '''
    возвращает индекс первого вхождения подстроки pattern в строке text
    :param text: анализируемая строка
    :param pattern: искомая подстрока
    :return: индекс первого вхождения подстроки в строке
    '''
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise ValueError('неверный тип данных')
    if len(pattern) > len(text):
        raise ValueError('Длина искомой подстроки не может быть больше длины строки')
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)].lower() == pattern.lower():
            return i
    return 'Искомая подстрока не найдена'

def find_elem(lst: list, value):
    '''
    возвращает индекс первого вхождения элемента value в списке lst
    :param lst: анализируемый список
    :param value: искомый элемент
    :return: индекс первого вхождения искомого элемента
    '''
    if not isinstance(lst, list) or not isinstance(value,(int,float,str)):
        raise TypeError('неверный тип данных')
    index_elem = 0
    for i in lst:
        if i == value:
            return index_elem
        index_elem += 1
    return 'искомых элементов в списке нет'

def count_occurrences(lst: list, value):
    '''
    возвращает количество вхождений элемента value в списке lst
    :param lst: анализируемый список
    :param value: искомый элемент
    :return: кол-во искомых элементов ванализируемом списке
    '''
    if not isinstance(lst, list) or not isinstance(value,(int,float,str)):
        raise ValueError('неверный тип данных')
    count_elem = 0
    for i in lst:
        if i == value:
            count_elem += 1
    return count_elem

def reverse_words(s: str):
    '''
    принимает строку из нескольких слов и возвращает новую строку, в которой порядок слов обратный исходному,
    :param s: анализируемая строка
    :return: слова исходной строки в обратном порядке
    '''
    if not isinstance(s, str):
        raise TypeError('неверный тип данных')
    final_lst = []
    for i in s.split():
        final_lst.insert(0,i)
    return ' '.join(final_lst) if final_lst != [] else 'исходная строка пуста'

def is_palindrome(s: str):
    '''
     проверяет, является ли переданная строка палиндромом (игнорируя регистр и пробелы)
    :param s: анализируемая строка
    :return: булиево значение является ли строка палиндромом
    '''
    if not isinstance(s, str):
        raise Typerror('неверный тип данных')
    string_only_symbol = [i for i in s if i.isalnum()]
    return string_only_symbol == string_only_symbol[::-1] if string_only_symbol != [] else 'исходная строка пуста'
