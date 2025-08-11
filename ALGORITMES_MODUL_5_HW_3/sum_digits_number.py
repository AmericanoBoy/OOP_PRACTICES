
import sys #импортируем сторонний модуль для увеличения глубины рекурсии в случае необходимости
def sum_digits_number(number: int) ->int:
    '''
    рекурсивная функция, вычисляющая сумму  составляющих цифр числа
    :param number: 1,3,4
    :return: 8
    '''

    if not isinstance(number, int): raise TypeError('ВХОДНЫЕ ДАННЫЕ ДОЛЖНЫ БЫТЬ ТИПОМ |int| !')
    bit_depth_number = len(str(number)) #определяем разрядность числа
    if bit_depth_number > 2000: raise ValueError('В КАЧЕСТВЕ АРГУМЕНТА ПОЛУЧЕНО СЛИШКОМ БОЛЬШОЕ ДЛЯ НАХОЖДЕНИЯ СУММЫ ЦИФР С ПОМОЩЬЮ РЕКУРСИИ !')
    limit_recursion = [1000, 10 + bit_depth_number][bit_depth_number > 995]  # вычисляем необходимый лимит рекурсии
    sys.setrecursionlimit(limit_recursion)  # увеличиваем встроенный лимит рекурсии в случае необходимости
    return number if number <= 10 else number % 10 + sum_digits_number(number // 10)

print(sum_digits_number(123))