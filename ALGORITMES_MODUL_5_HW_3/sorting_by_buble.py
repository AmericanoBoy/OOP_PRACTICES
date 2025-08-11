
def check_iter_data(data): #функция контроля принадлежности итерируемого эл_та к типу |int, float|
    if not isinstance(data, (int, float)): raise TypeError('ТИП ИТЕРИРУЕМОГО ЭЛ_ТА ДОЛЖЕН БЫТЬ |int, float| !')
    return data

def sort_buble(array: list, order_by=lambda x, y: x > y, key=lambda obj: obj)->list:
    if not isinstance(array, list): raise TypeError('ВХОДНЫЕ ДАННЫЕ ДОЛЖНЫ БЫТЬ ТИПОМ |list| !')
    change = True
    while change:
        change = False
        for i in range(len(array) - 1):
            if order_by(key(check_iter_data(array[i])), key(check_iter_data(array[i+1]))):
                array[i], array[i + 1] = array[i + 1], array[i]
                change = True
    return array
