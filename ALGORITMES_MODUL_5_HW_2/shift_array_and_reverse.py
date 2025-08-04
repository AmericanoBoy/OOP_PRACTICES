

# 'CПИСЫВАЛЬЩИКИ', НЕ ВОРУЕМ МОИ ИДЕИ, А ДУМАЕМ САМИ !!!   А ЕСЛИ КОПИРУЕТЕ - ССЫЛКА НА ОРИГИНАЛ ОБЯЗАТЕЛЬНА !!!!

def control_input_data(array,shift_flag):
    if not isinstance(array, list): raise TypeError('ИТЕРИРУЕМЫМ ОБЪЕКТОМ ДОЛЖЕН БЫТЬ СПИСКОМ !')
    if len(array) == 0: raise ValueError('ВХОДНОЙ СПИСОК  НЕ ДОЛЖЕН БЫТЬ ПУСТЫМ !')
    if not isinstance(shift_flag, int): raise TypeError('ГРАНИЦА СДВИГА ДОЛЖНА БЫТЬ ЦЕЛЫМ ЧИСЛОМ !')
    if shift_flag > len(array) or shift_flag < 0: raise ValueError('ДИАПАЗОНЫ ПОИСКА ДОЛЖНЫ БЫТЬ ДОПУСТИМЫМИ !')


#cдвиг списка на 'n' позиций вправо и инверсия

def shift_array_right_and_reverse(array, shift_flag):
    '''
    функция, cдвигающая список 'array' на 'shift_flag' позиций вправо,
    а затем инверсирует полученный список
    :param array, shift_flag: [1,2,3,4,5,6,7,8], 3
    :return: [3,2,1,8,7,6,5,4]
    примечание: сложность алгоритма Оn. Прицип алгоритма основан не на
    'cначала сдвиге вправо' а потом инверсии....
    Алгоритм максимально упрощен: инверсируются между собой элементы
    до 'shift_flag' и после 'shift_flag'
    '''

    control_input_data(array, shift_flag) #проверяем допустимость входных данных
    len_array = len(array) #длина списка
    half_shift_flag_and_len_array = int(shift_flag/2) #'точка инверсии' сдвига второй части списка
    half_shift_flag_and_0 = int((len_array - shift_flag)/2) #'точка инверсии' сдвига первой части списка
    difference_between_len_array_and_shift_flag = len_array-shift_flag #граница инверсии первой части списка
    limit_cycle_range = len_array - half_shift_flag_and_len_array #лимит итераций цикла 'range'

    count = 0
    for i in range(limit_cycle_range):
        if i < half_shift_flag_and_0:
            temp_variable = array[i]
            array[i] = array[difference_between_len_array_and_shift_flag-i-1]
            array[difference_between_len_array_and_shift_flag-i-1] = temp_variable
        if i >= difference_between_len_array_and_shift_flag:
            count += 1
            temp_variable = array[i]
            array[i] = array[len_array-count]
            array[len_array-count] = temp_variable

    return array

#_________________________________________________________________________________________________________________

#cдвиг списка на 'n' позиций влево и инверсия

def shift_array_left_and_reverse(array, shift_flag):
    '''
    функция, cдвигающая список 'array' на 'shift_flag' позиций влево,
    а затем инверсирует полученный список
    :param array, shift_flag: [1,2,3,4,5,6,7,8], 3
    :return: [3,2,1,8,7,6,5,4]
    примечание: сложность алгоритма Оn. Прицип алгоритма основан не на
    'cначала сдвиге влево' а потом инверсии....
    Алгоритм максимально упрощен: инверсируются между собой элементы
    до 'shift_flag' и после 'shift_flag'
    '''

    control_input_data(array, shift_flag) #проверяем допустимость входных данных
    len_array = len(array) #длина списка
    half_shift_flag_and_len_array = int((len_array-shift_flag)/2) #'точка инверсии' сдвига первой части списка
    limit_cycle_range = len_array - half_shift_flag_and_len_array #лимит итераций цикла 'range'
    count = 0
    for i in range(limit_cycle_range):
        if i < int(shift_flag/2):
            temp_variable = array[i]
            array[i] = array[shift_flag-i-1]
            array[shift_flag-i-1] = temp_variable
        if i >= shift_flag:
            count += 1
            temp_variable = array[i]
            array[i] = array[len_array-count]
            array[len_array-count] = temp_variable

    return array




