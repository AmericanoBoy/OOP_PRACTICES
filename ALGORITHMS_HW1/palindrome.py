
def calculating_palindrome(number: int)-> bool:

    #обрабатываем ошибки и исключения
    if not isinstance(number, int): raise TypeError('Тип входных данных должен быть |int| !')
    if number < 0 or number > int((2**31)-1): raise ValueError('НЕДОПУСТИМЫЙ РАЗМЕР ВХОДНЫХ ДАННЫХ !')

    #задаем переменную, куда будем 'сладывать' числа с конца исходного числа
    palindrome = 0
    #cоздаем копию исходной входной переменной для последующего сравнительного анализа
    copy_number = number

    while number > 0:

        palindrome = palindrome * 10 + (number % 10)
        number = number // 10

        #если число, анализируем с конца совпадают с анализируемыми с начала- возвращаем True
        if palindrome == number: return True

    #если функция не вернула True - проводим заключительный анализ сравнения
    return palindrome == copy_number

print(calculating_palindrome(12321))