
def count_ones_in_bin_number(number: int)-> int:

    '''
    функция для нахождения кол_ва единиц в двоичном представлении исходного числа
    :param number: 127
    :return: 7
    '''

    #обрабатываем ошибки и исключения
    if not isinstance(number, int): raise TypeError('Тип введенных данных должен быть |int| !')
    if number < 0: raise ValueError('Введенное число должно быть больше нуля !')

    #объявляем переменную счетчика кол_ва единиц в двоичном представлениии числа
    counter_ones = 0

    #сoдаем цикл в котором будем делить исходное число на два, используя остаток от деления на 2 в качестве кол_ва единиц
    while number > 0:
        counter_ones += (number % 2)
        number = int(number / 2)

    return counter_ones

print(count_ones_in_bin_number(13))