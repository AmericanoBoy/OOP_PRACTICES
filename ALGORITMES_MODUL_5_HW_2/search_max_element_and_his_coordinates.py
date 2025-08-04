

# 'CПИСЫВАЛЬЩИКИ', НЕ ВОРУЕМ МОИ ИДЕИ, А ДУМАЕМ САМИ !!!  А ЕСЛИ КОПИРУЕТЕ - ССЫЛКА НА ОРИГИНАЛ ОБЯЗАТЕЛЬНА !!!!

def control_input_data(array,start,end):
    if not isinstance(array, list): raise TypeError('ИТЕРИРУЕМЫМ ОБЪЕКТОМ ДОЛЖЕН БЫТЬ СПИСКОМ !')
    if len(array) == 0: raise ValueError('ВХОДНОЙ СПИСОК  НЕ ДОЛЖЕН БЫТЬ ПУСТЫМ !')
    if start < 0 or end > len(array): raise ValueError('ДИАПАЗОНЫ ПОИСКА ДОЛЖНЫ БЫТЬ ДОПУСТИМЫМИ !')

def control_iteration_data(data):
    if not isinstance(data, (int, float)): raise TypeError('ЭЛЕМЕНТ ДОЛЖЕН БЫТЬ ЧИСЛОМ ТИПА: INT|FLOAT !')

def max_in_range_between_start_and_end(array, start, end):
    '''
    функция нахождения максимального числа и его абсолютной и относительной координаты в указанном диапазоне индексов списка
    возвращает список из трех элементов, где: первый- сам макс. элемент, второй- абсол. коорд., третий- относит. координата
    :param array, start, end: [3, 2, 4, 5, 7, 2, 5, 1], 1, 6
    :return: [7, 4, 3]
    '''

    control_input_data(array, start, end)

    index_max_i, relative_index_max = start, 0
    count_relative = 0
    for i in range(start+1, end + 1):

        control_iteration_data(array[i])

        if array[i] >= array[index_max_i]:
            index_max_i = i
            relative_index_max = index_max_i - count_relative - 1
        count_relative += 1
    lst_index_max_relative_and_absolut = [array[index_max_i], index_max_i, relative_index_max]
    return lst_index_max_relative_and_absolut

#array = [1,3,5,4,6,2,4,5,3]
#print(max_in_range_between_start_and_end(array,2,6))