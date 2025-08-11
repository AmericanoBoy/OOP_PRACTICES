
def check_iter_data(data): #функция контроля принадлежности итерируемого эл_та к типу |int, float|
    if not isinstance(data, (int, float)): raise TypeError('ТИП ИТЕРИРУЕМОГО ЭЛ_ТА ДОЛЖЕН БЫТЬ |int, float| !')
    return data

def sort_choice(array: list, order_by=lambda x, y: x < y, key=lambda obj: obj)->list:
    if not isinstance(array, list): raise TypeError('ВХОДНЫЕ ДАННЫЕ ДОЛЖНЫ БЫТЬ ТИПОМ |list| !')
    len_array = len(array)
    count = 0
    array_rearranged_elements = []
    while count < len_array - 1:
        temp = count
        j = count + 1
        while j < len_array:
            if order_by(key(check_iter_data(array[j])), key(check_iter_data(array[temp]))):
                temp = j
            j += 1
        array[count], array[temp] = array[temp], array[count]
        array_rearranged_elements.append([array[count], array[temp]])
        count += 1

    return f'Oтсорт. список: {array}\n'\
           f'Список поэтапно переставляемых эл_ов: {array_rearranged_elements}\n'\
           f'Произведено {count}  этапов cравнений и обмена элементов списка.'

print(sort_choice([1,4,6,-1,3.5,0]))