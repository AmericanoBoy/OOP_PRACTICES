
# ----- List (Список/Динамический массив) -----

# Fields (Атрибуты)
# - count -- фактическое кол-во элементов в массиве
# - size -- кол-во свободных ячеек памяти

# Interface (Операции)

# - add(elem) -- добавить элемент в конец списка
# - add_first(elem) -- добавить элемент в начало списка
# - insert(index, elem) -- вставить элемент на позицию

# - remove(elem) -- удалить элемент. если таких элементов много, удалить первое вхождение
# - pop(index) -- удалить элемент по индексу

# - find(elem) -- найти координату элемента. если таких элементов много, вернуть координату первого вхождения. если таких элементов нет, вернуть -1
# - count(elem) -- посчитать количество вхождений переданного элемента

# - max_elem(memory) -- поиск макс. значения списка
# - min_elem(memory) -- поиск мин. значения списка

# - clear() -- очистить массив (сделать каждый элемент None)
# - is_empty() -- проверка на пустоту массива


# - count - свойство, которое возвращает фактическое кол-во элементов

# ----------- Функции языка C -----------
def malloc(numbers): #создание пустого списка фиксированной длины
    return [None] * numbers

def realloc(old_memory, old_size, new_size): #расширение списка и заполнение неиспользуемых индексов 'пустотой'
    new_memory = malloc(new_size)

    for i in range(0, old_size, 1):
        new_memory[i] = old_memory[i]

    return new_memory

def check_index(search_index, count): #проверка на тип данных |int| при поиске, вствке элемента по индексу и допустимости индекса
    if not isinstance (search_index, int): raise TypeError('ИСКОМЫЙ ИНДЕКС ДОЛЖЕН БЫТЬ ЦЕЛЫМ ЧИСЛОМ !!!')
    if search_index > count: raise ValueError('ИСКОМЫЙ ИНДЕКС ДОЛЖЕН БЫТЬ МЕНЬШЕ ДЛИНЫ СУЩЕСТВУЮЩЕГО СПИСКА !!!')
    return search_index


def check_type_elem(count, memory): #проверка на принадлежность всех элементов списка к одному типу данных
    type_elem = type(memory[0])
    for i in range(1, count, 1):
        if type(memory[i]) != type_elem:
            raise TypeError('ИТЕРИРУЕМЫЕ ЭЛЕМЕНТЫ РАЗНЫХ ТИПОВ ДАННЫХ НЕ СРАВНИВАЮТСЯ !!!')
    return [memory, type_elem]


def max_and_min_if_all_elem_int(memory, count): #поиск макс. и мин. значения списка, если все типы итер. эл_ов == |int|
    max_elem, min_elem = memory[0], memory[0]
    for i in range(1, count, 1):
        if memory[i] > max_elem:
            max_elem = memory[i]
        if memory[i] < min_elem:
            min_elem = memory[i]
    return [max_elem, min_elem]

def count_elem_in_iter_elem(array): #вспомогательная функция поиска длины итерируемых элементов
    count = 0
    for i in array:
        count += 1
    return count

def max_and_min_all_elem_list(memory, count): #поиск. макс. и мин. значения списка, если все типы итер. эл_ов == |list|
    max_count, min_count = count_elem_in_iter_elem(memory[0]), count_elem_in_iter_elem(memory[0])
    max_elem, min_elem = memory[0], memory[0]

    for i in range(1, count, 1):
        if count_elem_in_iter_elem(memory[i]) > max_count:
            max_count = count_elem_in_iter_elem(memory[i])
            max_elem = memory[i]
        if count_elem_in_iter_elem(memory[i]) < mix_count:
            max_count = count_elem_in_iter_elem(memory[i])
            min_elem = memory[i]

    return [max_elem, min_elem]

def ord_elem_in_iter_elem(elem): #вспомогательная функция поиска суммарного значения |ord| итерируемого элемента
    count = 0
    for i in elem:
        count += ord(i)
    return count

def max_and_min_all_elem_str(memory, count): #поиск макс. и мин. значения списка, когда все типы итер. эл_ов == |str|
    max_ord, min_ord = ord_elem_in_iter_elem(memory[0]), ord_elem_in_iter_elem(memory[0])
    max_elem, min_elem = memory[0], memory[0]

    for i in range(1, count, 1):
        if ord_elem_in_iter_elem(memory[i]) > max_ord:
            max_ord = ord_elem_in_iter_elem(memory[i])
            max_elem = memory[i]
        if ord_elem_in_iter_elem(memory[i]) < min_ord:
            min_ord = ord_elem_in_iter_elem(memory[i])
            min_elem = memory[i]

    return [max_elem, min_elem]

# ----------- Реализация списка -----------

class List:

    __count: int
    __size: int

    def __init__(self):
        self.__count = 0
        self.__size = 5
        self.__memory = malloc(self.__size)




    def add(self, elem: any) -> None: #добавление элемента в конец списка

        if self.__count == self.__size:
            new_size = self.__size + self.__size // 2
            self.__memory = realloc(self.__memory, self.__size, new_size)
            self.__size = new_size

        self.__memory[self.__count] = elem
        self.__count += 1


    def add_first(self, elem: any) -> None: ##добавление элемента в начало списка

        if self.__count == self.__size:
            new_size = self.__size + self.__size // 2
            self.__memory = realloc(self.__memory, self.__size, new_size)
            self.__size = new_size

        for i in range( 0,self.__count+1):
            temp = self.__memory[i]
            self.__memory[i] = elem
            elem = temp
        self.__count += 1

    def insert(self, index: int, elem: any) -> None: ##добавление элемента в список по индексу

        search_index = check_index(index, self.__count)

        if self.__count == self.__size:
            new_size = self.__size + self.__size // 2
            self.__memory = realloc(self.__memory, self.__size, new_size)
            self.__size = new_size

        for i in range(search_index, self.__count+1):
            temp = self.__memory[i]
            self.__memory[i] = elem
            elem = temp
        self.__count += 1

    def remove(self, elem: any) -> None:

        target_position = -1

        for i in range(0, self.__count, 1):
            if self.__memory[i] == elem:
                target_position = i
                break

        if target_position == -1: return

        for i in range(target_position, self.__count - 1, 1):
            self.__memory[i] = self.__memory[i + 1]

        self.__count -= 1
        self.__memory[self.__count] = None

    def pop(self, index: int) -> None: ##удаление элемента списка по индексу

        search_index = check_index(index, self.__count)

        for i in range(search_index, self.__count+1):
            self.__memory[i] = self.__memory[i+1]
        self.__count -= 1


    def find(self, elem: any) -> int: ##нахождение индекса искомого элемента списка

        target_position = -1

        for i in range(0, self.__count, 1):
            if elem == self.__memory[i]:
                target_position = i
                break

        return target_position

    def count_elem(self, elem: any) -> int: ##кол-во вхождений искомого элемента в список

        count_elem = 0

        for i in range(0, self.__count, 1):
            if elem == self.__memory[i]:
                count_elem += 1

        return count_elem


    def max_elem(self) -> any: #поиск макс. значения списка при итер. эл_ах == |int,float or list or str|
        if self.__count == 0: return -1
        if self.__count == 1: return self.__memory[0]
        memory = check_type_elem(self.__count, self.__memory)
        if memory[1] == int: return max_and_min_if_all_elem_int(self.__memory, self.__count)[0]
        if memory[1] == list: return max_and_min_all_elem_list(self.__memory, self.__count)[0]
        if memory[1] == str: return max_and_min_all_elem_str(self.__memory, self.__count)[0]

    def min_elem(self) -> any: #поиск макс. значения списка при итер. эл_ах == |int,float or list or str|
        if self.__count == 0: return -1
        if self.__count == 1: return self.__memory[0]
        memory = check_type_elem(self.__count, self.__memory)
        if memory[1] == int: return max_and_min_if_all_elem_int(self.__memory, self.__count)[1]
        if memory[1] == list: return max_and_min_all_elem_list(self.__memory, self.__count)[1]
        if memory[1] == str: return max_and_min_all_elem_str(self.__memory, self.__count)[1]



    def clear(self) -> None: #очистка списка

        if self.__count != 0:
            for i in range(0, self.__count, 1):
                self.__memory[i] = None


    def is_empty(self) -> bool: #проверка списка на пустоту

        return [False, True][self.__count == 0]

    def len(self) -> int: #общее кол-во элементов списка (длина списка)

        return self.__count

    def __get_count(self):
        return self.__count
    count = property(__get_count)

    def __get_memory(self):
        return self.__memory
    memory = property(__get_memory)

    def __get_size(self):
        return self.__size
    size = property(__get_size)

