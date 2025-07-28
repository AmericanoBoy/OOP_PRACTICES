import  time


def factorial_of_number_low_search_speed(number: int)-> int:
    '''
    функция принимает на вход число и вовращает факторал этого числа
    скорость выполнения низкая (факториал числа 100000 находит в течении от 8 до 9 секунд)
    алгоритм построен по принципу постепенного перемножения между собой чисел
    в цифровом ряде от 1 до искомого числа
    :param number: 100000
    :return: fact(100000)
    '''

    if not isinstance(number, int):
        raise TypeError('ТИП ВВЕДЕННЫХ ДАННЫХ ДОЛЖЕН БЫТЬ ЧИСЛОМ !')
    if number < 0:
        raise ValueError('ФАКТОРИАЛ НЕ МОЖЕТ БЫТЬ НАЙДЕН ИЗ ЧИСЛА МЕНЬШЕ НУЛЯ !')
    if number > 20:
        raise ValueError('ВВИДУ МАЛОЙ СКОРОСТИ АЛГОРИТМА ВВЕДЕННОЕ ЧИСЛО НЕ МОЖЕТ БЫТЬ БОЛЬШЕ 20 !')

    result = 1
    for i in range(1, number+1):
        result *= i
    return result

def factorial_of_number_average_search_speed(number: int)-> int:
    '''
    функция принимает на вход число и вовращает факторал этого числа
    скорость выполнения cредняя (факториал числа 100000 находит в течении от 4 до 5 секунд)
    алгритм построен на разбиении цифрового ряда от 1 до искомого числа на две части
    и перемножения элементов между собой
    (т.к. при вычислении электронная машина быстрее перемножает между собой числа
    приблизительно одинакой длины и разрядности)
    :param number: 100000
    :return: fact(100000)
    '''

    if not isinstance(number, int):
        raise TypeError('ТИП ВВЕДЕННЫХ ДАННЫХ ДОЛЖЕН БЫТЬ ЧИСЛОМ !')
    if number < 0:
        raise ValueError('ФАКТОРИАЛ НЕ МОЖЕТ БЫТЬ НАЙДЕН ИЗ ЧИСЛА МЕНЬШЕ НУЛЯ !')

    result_1, result_2 = 1, 1
    half_of_number = number//2
    control_result_2 = 0
    for i in range(1, half_of_number+1):
        result_1 *= i
        result_2 *= (i + half_of_number)
        control_result_2 = i + half_of_number
    return [result_1 * result_2, (result_1 * result_2) * number][control_result_2 != number]

def factorial_of_number_high_search_speed(number: int)-> int:

    '''
    функция принимает на вход число и вовращает факторал этого числа
    скорость выполнения cредняя (факториал числа 100000 находит в течении 1 секунды)
    алгритм построен на постепенном разбиении цифрового ряда от 1 до искомого числа
    на попарные элементы приблизительно одинаковой длины
    при этом, если длина цифрового ряда нечетна- последний элемент остаетя неизменным
    (т.к. при вычислении электронная машина быстрее перемножает между собой числа
    приблизительно одинакой длины и разрядности)
    пример: факториал 7
                         -> 1,2,3,4,5,6,7
                         -> 2,12,30,7 (т.е: 1*2, 3*4, 5*6, 7)
                         -> 24, 210 ( т.е: 2*12, 30*7)
                         -> возвращает: 5040 (т.е: 24*210)
    :param number: 100000
    :return: fact(100000)
    '''

    if not isinstance(number, int):
        raise TypeError('ТИП ВВЕДЕННЫХ ДАННЫХ ДОЛЖЕН БЫТЬ ЧИСЛОМ !')
    if number < 0:
        raise ValueError('ФАКТОРИАЛ НЕ МОЖЕТ БЫТЬ НАЙДЕН ИЗ ЧИСЛА МЕНЬШЕ НУЛЯ !')
    if number == 0: return 1

    array_temp = [i for i in range(1, number+1)]
    len_array_temp = None
    while len_array_temp != 1:
        len_array_temp = len(array_temp)
        last_item_array_temp=array_temp[-1]
        array_temp=[array_temp[i]*array_temp[i+1] for i in range(0,len_array_temp-1,2)]
        if len_array_temp % 2 != 0:
            array_temp = array_temp+[last_item_array_temp]
    return [array_temp[0], array_temp[0] * array_temp[-1]][len_array_temp == 2]

#print(factorial_of_number_low_search_speed(100000))
#print(factorial_of_number_average_search_speed(100000))
print(factorial_of_number_high_search_speed(10))