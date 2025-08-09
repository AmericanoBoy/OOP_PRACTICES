

# 'CПИСЫВАЛЬЩИКИ', НЕ ВОРУЕМ МОИ ИДЕИ, А ДУМАЕМ САМИ !!!   А ЕСЛИ КОПИРУЕТЕ - ССЫЛКА НА ОРИГИНАЛ ОБЯЗАТЕЛЬНА !!!!

def control_input_data(array):
    if not isinstance(array, list): raise TypeError('ИТЕРИРУЕМЫМ ОБЪЕКТОМ ДОЛЖЕН БЫТЬ СПИСКОМ !')
    if len(array) == 0: raise ValueError('ВХОДНОЙ СПИСОК НЕ ДОЛЖЕН БЫТЬ ПУСТЫМ !')
def control_iteration_data(data):
    if not isinstance(data, (int, float)): raise TypeError('ЭЛЕМЕНТ ДОЛЖЕН БЫТЬ ЧИСЛОМ ТИПА: INT|FLOAT !')


def reverse_only_even_numbers_array(array):
    '''
    функция принимает на вход список и возвращает новый список, в котором
    только четные числа идут в обратном порядке
    :param array: [3, 2, 4, 5, 7, 6, 5, 1]
    :return: [3, 6, 4, 5, 7, 2, 5, 1]

    примечание: чтобы избежать обрботки дополнительно вложенных списков, и, как следствие, сложности Оn^2,
    cоздана функция, имеющая сложность Оn и позволющая выполнить задачу в один 'проход' списка.
    Прицип работы функции состоит в методе 'cужающегося окна': т.е. начинаем итерацию 'cлева',
    находим индекс четного эл_та, фиксируем его для того чтобы в последующем реверсировать элемент,
    фиксируем этот индекс, чтобы в последующем продолжить итерацию именно с этого индекса
    и начинаем итерацию 'справа' повторяя все предыдущие действия.
    Затем также циклически возврашаемся то 'влево', то 'вправо', пока не проитерируем все элементы
    и не 'реверсируем' все его четные элементы.
    '''

    control_input_data(array)
    len_array = len(array) #определяем длину списка
    flag_even_number = False #переменная, являющуяся сигналом при нахождении четного элемента
    total_count_iterations = 0 #переменная, считающая общее кол_во итерируемых эл_ов
    count_iterations_left, count_iterations_right = 0, 0 #переменные, считающие итерируемые эл_ты слева и справа
    index_left_even_number, index_right_even_number = 0, 0 #переменные, хранящие в себе индексы четных эл_ов при отсчете 'слева' и 'справа'

    while True:

        if flag_even_number == False:
            for i in range(count_iterations_left, len_array, 1): #итерируем 'cлева направо'
                control_iteration_data(array[i])
                count_iterations_left += 1 #считаем итеруемые эл_ты слева
                total_count_iterations += 1 #cчитаем общее кол_во итерируемых эл_ов
                if array[i] % 2 == 0: #находим четный элемент
                    index_left_even_number = count_iterations_left - 1 #определяем индекс 'левого' элемента для реверса и фиксируем его
                    flag_even_number = True #передаем в переменную противоположное значение, сигнализирующую, что теперь итерация будет 'справа'
                    break
        if flag_even_number == True:
            for i in range(len_array-1-count_iterations_right, 0, -1): #итерируем 'справа налево'
                control_iteration_data(array[i])
                count_iterations_right += 1 #считаем итеруемые эл_ты справа
                total_count_iterations += 1 #cчитаем общее кол_во итерируемых эл_ов
                if array[i] % 2 == 0: #находим четный элемент
                    index_right_even_number = len_array - count_iterations_right #определяем индекс 'правого' элемента для реверса и фиксируем его
                    flag_even_number = False #передаем в переменную противоположное значение, сигнализирующую, что теперь итерация будет 'слева'
                    break


        array[index_left_even_number], array[index_right_even_number] = array[index_right_even_number],array[index_left_even_number] #меняем местами четные 'левые' и 'правые' элементы

        if total_count_iterations >= len_array: #в случае если мы проитетировали все элементы списка....
            return array #возвращаем список, в котором все четные эл_ты идут в обратном порядке

#array=[1,2,4,5,3,4,12,6,2,1,1,6,8,1,5,7,3,5,9]
#print(reverse_only_even_numbers_array(array))

