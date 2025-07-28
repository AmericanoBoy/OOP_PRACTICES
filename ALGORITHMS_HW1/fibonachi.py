
import decimal

def create_fibonachi_array_1_option(number: int)-> list:

    '''
    функция нахождения списка чисел фибоначи от 1 до заданного числа
    алгорит построен на принципе нахождения последующего элемента
    списка путем сложения двух предыдущих элементов
    :param number: 6
    :return: [0,1,1,2,3,5]
    '''

    # обрабатываем ошибки и исключения
    if not isinstance(number, int):
        raise TypeError('В КАЧЕСТВЕ ВХОДНЫХ ДАННЫХ ДОЛЖНО БЫТЬ ЧИСЛО !')
    if number < 0:
        raise ValueError('ВХОДНЫЕ ДАННЫЕ НЕ МОГУТ БЫТЬ МЕНЬШЕ НУЛЯ !')

    #cоздаем исходный список для дальнейших расчетов
    start_fibonachi_aray = [0, 1]

    # если входной параметр меньше трех - сразу выводим список не заходя в цикл
    if number < 3: return start_fibonachi_aray[:number+1]

    #объявляем переменную являющуюся суммой между аоследним и предпоследним элементами списка ряда фибоначи
    sum_too_last_items = start_fibonachi_aray[-1] + start_fibonachi_aray[-2]
    #объявляем счетчик кол_ва эл_ов ряда фибоначи
    count_remaining_items = number - 2
    while count_remaining_items != 0:
        #добавляем к переменой, являющуюся суммой в список фибоначи
        start_fibonachi_aray.append(sum_too_last_items)
        #к переменной, являющуюся суммой прибавляем предпоследний элемент списка фибоначи
        sum_too_last_items += start_fibonachi_aray[-2]
        count_remaining_items -= 1

    return start_fibonachi_aray

def create_fibonachi_array_2_option(number: int)-> list:

    '''
    функция нахождения списка чисел фибоначи от 1 до заданного числа
    алгорит построен на принципе первоначального нахождения
    последнего и предпоследнего элемента списка путем вычисления по формуле фибоначи
    затем получаем предыдущие элементы путем вычитания
    первого элемента списка из второго
    :param number: 7
    :return: [0,1,1,2,3,5,8]
    '''

    #обрабатываем ошибки и исключения
    if not isinstance(number, int):
        raise TypeError('В КАЧЕСТВЕ ВХОДНЫХ ДАННЫХ ДОЛЖНО БЫТЬ ЧИСЛО !')
    if number < 0:
        raise ValueError('ВХОДНЫЕ ДАННЫЕ НЕ МОГУТ БЫТЬ МЕНЬШЕ НУЛЯ !')

    #если входной параметр меньше трех - сразу выводим список не заходя в цикл
    if number < 3: return [0, 1][:number+1]

    #устанавливаем значение точности до 10000 цифр
    decimal.getcontext().prec = 10000

    #используя модуль decimal, находим корень из пяти без погрешностей
    square_root_of_5 = decimal.Decimal(5).sqrt()

    # oпределяем константу 'золотого сечения'
    const_gold_ratio = ((1 + square_root_of_5) / 2)

    #используя константы 'золотого сечения' находим прелпоследний и последний элемент чичлового ряда фибоначи
    last_element = round(((const_gold_ratio ** (number-1)) - ((-const_gold_ratio) ** (-number-1))) / square_root_of_5)
    the_penultimate_element = round(((const_gold_ratio ** (number-2)) - ((-const_gold_ratio) ** (-number-1))) / square_root_of_5)

    #вносим найденные элементы в начальный список
    start_fibonachi_aray = [the_penultimate_element, last_element]
    #cоздаем счетчик для подсчета кол_ва эл_ов ряда
    count_element_start_fibonachi_aray = 2

    #постепенно вычитая первый эл_нт списка из второго и внося его в исходный список, доходим до первого числа
    while count_element_start_fibonachi_aray < number:
        next_element = start_fibonachi_aray[1] - start_fibonachi_aray[0]
        start_fibonachi_aray.insert(0, next_element)
        count_element_start_fibonachi_aray += 1

    return start_fibonachi_aray

print(create_fibonachi_array_1_option(1))
print(create_fibonachi_array_2_option(1))