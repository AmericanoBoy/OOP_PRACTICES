

# 'CПИСЫВАЛЬЩИКИ', НЕ ВОРУЕМ МОИ ИДЕИ, А ДУМАЕМ САМИ !!! А ЕСЛИ КОПИРУЕТЕ - ССЫЛКА НА ОРИГИНАЛ ОБЯЗАТЕЛЬНА !!!!

def control_input_data(array):
    if not isinstance(array, list): raise TypeError('ИТЕРИРУЕМЫМ ОБЪЕКТОМ ДОЛЖЕН БЫТЬ СПИСКОМ !')
    if len(array) == 0: raise ValueError('ВХОДНОЙ СПИСОК НЕ ДОЛЖЕН БЫТЬ ПУСТЫМ !')
def control_iteration_data(data):
    if not isinstance(data, int): raise TypeError('ЭЛЕМЕНТ ДОЛЖЕН БЫТЬ ЧИСЛОМ ТИПА: INT|FLOAT !')


#1 вариант решения (в процессе итерации проверяем тип данных каждого элемента списка):

def increase_number_list_by_one(array):
    '''
    функция, преобразующая входной список по принципу сложения 'числа' списка с числом один
    :param array: [1, 2, 7, 9]
    :return: [1, 2, 8, 0]
    прим:
    1.перед началом цикла проверяем входные данные на принадлежность входных данных к типу |list|
    2.в теле цикла с помощью сторонней функции 'control_iteration_data' проверяем принадлежность каждого элемента к типу данных |int|
    '''

    control_input_data(array)

    flag = False #т.к. проверяем все элементы на тип данных- создаем переменную, которая будет 'фиксировать' наличие в списке цифры '9'
    for i in range(len(array)-1, -1, -1):

        control_iteration_data(array[i])
        
        if array[i] != 9 and flag == False:
            array[i] += 1
            flag = True
        elif array[i] == 9 and flag != True:
            array[i] = 0

    return [[1] + array, array][flag == True]

#2 вариант решения (без проверки типа данных итерируемых элементов):

def increase_number_list_by_one_without_control_iteration_element(array):
    '''
    функция, преобразующая входной список по принципу сложения 'числа' списка с числом один
    :param array: [1, 2, 7, 9]
    :return: [1, 2, 8, 0]
    прим: перед началом цикла проверяем входные данные на принадлежность входных данных к типу |list|
    '''

    control_input_data(array)

    for i in range(len(array)-1, -1, -1):
        if array[i] != 9:
            array[i] += 1
            return array
        array[i] = 0
    return [1] + array
        


#array=[1,2,3,4,5,9,6,7,8,9,9]
#array =[9,9,9]

#print(increase_number_list_by_one(array))
