import csv
import os
import os.path
import datetime

#1 вариант решения проблемы (наиболее скоростной и упрощенный)
def search_days_and_months_withs_max_sales_withs_high_speed_algorithm(file_name):

    '''
    функция собирает данные о продажах из электронной таблицы в формате 'csv',
    упковывает  их данные в двумерный список в формате: дата|кол_во продаж,
    исключая при этом дни недели и месяцы, когда магазин не работал (ввод некорректных данных)
    и выводит таблицы с продажами выше и ниже средних по неделям и месяцам
    :param file_name: date,visitors \n 2023-01-01,150  \n 2023-01-02,200 и т.д.
    :return: список дней недели с продажами выше среднего: вторник, суббота и т.д.
             список месяцев с продажами выше среднего: январь и т.д.
             список дней недели с продажами ниже среднего: средаЮ четверг и т.д.
             список месяцев с продажами ниже среднего: февраль и т.д.
    '''

    '''проверяем расширение в названии файла'''
    basename, extension = os.path.splitext(file_name)
    if extension != '.csv':
        raise NameError('НЕВЕРНЫЙ ФОРМАТ ВВОДНЫХ ДАННЫХ !')

    '''проверяем существует ли файл'''
    if os.path.exists(file_name) != True:
        raise FileNotFoundError('ИСКОМОГО ВАМИ ФАЙЛА НЕ СУЩЕСТВУЕТ !')

    '''
    создаем двумерный список, где первый элемент каждого вложенного списка является указателем дня недели,
    а второй- счетчиком продаж по этому дню недели
    '''
    sales_lst_by_days_of_the_week = [
                                       ['понедельник', 0],
                                       ['вторник', 0],
                                       ['среда', 0],
                                       ['четверг', 0],
                                       ['пятница', 0],
                                       ['суббота', 0],
                                       ['воскресенье', 0]
                                    ]

    '''
    создаем двумерный список, где первый элемент каждого вложенного списка является указателем месяца,
    а второй- счетчиком продаж по этому месяцу
    '''
    sales_lst_by_months = [
                          ['январь', 0],
                          ['февраль', 0],
                          ['март', 0],
                          ['апрель', 0],
                          ['май', 0],
                          ['июнь', 0],
                          ['июль', 0],
                          ['август', 0],
                          ['сентябрь', 0],
                          ['октябрь', 0],
                          ['ноябрь', 0],
                          ['декабрь', 0]
                        ]

    '''
    cоздаем пустое множество в которое будут заносится порядковые номера дней недели, 
    в которые магазин реально работал. 
    структура данных 'множество' поможет нам избежать дублирования порядковых номеров
    дней недели и автоматически отсортирует их в порядке возрастания
    '''
    array_control_real_work_shop_by_days_of_the_week = set()

    '''
    cоздаем пустое множество в которое будут заносится порядковые номера месяцев, 
    в которые магазин реально работал. 
    структура данных 'множество' поможет нам избежать дублирования порядковых номеров
    месяцев и автоматически отсортирует их в порядке возрастания
    '''
    array_control_real_work_shop_to_months = set()

    '''счетчик тотальных продаж за весь рассматриваемый период времени'''
    total_sales = 0

    with open(file_name, 'r',encoding ='utf-8') as file:

        '''преобразовываем входные данные в список для удобства обработки'''
        csv_reader = [i for i in csv.reader(file)]

        for row in csv_reader[1:]:

            '''обрабатываем исключение длины строки в формате: дата, кол_во продаж'''
            if len(row) != 2:
                raise ValueError('НЕСООТВЕТСТВУЮЩАЯ ФОРМАТУ (ДАТА|КОЛ_ВО ПРОДАЖ) СТРОКА !')

            '''преобразовываем информацию о датах в список'''
            array_date = row[0].split('-')

            '''обрабатываем исключение на соответствие формату даты'''
            if len(array_date) != 3:
                raise ValueError('НЕСООТВЕТСТВУЮЩАЯ ФОРМАТУ (ГОД|МЕСЯЦ|ЧИСЛО) ДАТА ! ')

            '''вычисляем дни недели дат в модуле дататайм и обрабатываем исключение на несуществующую дату'''
            try: date = datetime.datetime(int(array_date[0]), int(array_date[1]), int(array_date[2]))
            except: raise ValueError('УКАЗАНА НЕСУЩЕСТВУЮЩАЯ ДАТА !')

            '''преобразоваваем данные о дневной выручке в тип данных |int| и обрабатываем исключения'''
            try: daily_sales = int(row[-1])
            except: raise TypeError('НЕВОЗМОЖНО ПРЕОБРАЗОВАТЬ ДАННЫЕ В ЧИСЛО !')

            '''заносим данные о продажах по каждому дню недели в список продаж по неделям'''
            sales_lst_by_days_of_the_week[date.isoweekday() - 1][-1] += daily_sales
            '''заносим в  множество номера днней недели, в которые магазин работал'''
            array_control_real_work_shop_by_days_of_the_week.add(date.isoweekday())
            '''заносим данные о продажах по каждому месяцу в список'''
            sales_lst_by_months[int(array_date[1]) - 1][-1] += daily_sales
            '''заносим в множество номера месяцев, в которые магазин работал'''
            array_control_real_work_shop_to_months.add(int(array_date[1]))

            '''суммируем счетчик тотальных продаж'''
            total_sales += daily_sales


        '''вычисляем среднее значение продаж по дням недели, в которые магазин реально работал'''
        average_sales_by_day_of_the_week = int(total_sales / len(array_control_real_work_shop_by_days_of_the_week))
        '''вычисляем среднее значение продаж по месяцам, в которые магазин реально работал'''
        average_number_of_sales_by_month = int(total_sales / len(array_control_real_work_shop_to_months))


        '''выбираем из заполненного списка продаж по дням недели дни с выручкой выше или равные средней выручке'''
        array_titles_days_of_the_week_with_max_sales = [sales_lst_by_days_of_the_week[i-1][0] for i in array_control_real_work_shop_by_days_of_the_week if sales_lst_by_days_of_the_week[i-1][-1] >= average_sales_by_day_of_the_week]
        '''выбираем из заполненного списка продаж по месяцам те месяца, где выручка выше или равна средней'''
        array_titles_months_with_max_sales = [sales_lst_by_months[i-1][0] for i in array_control_real_work_shop_to_months if sales_lst_by_months[i-1][-1] >= average_number_of_sales_by_month]

        '''выбираем из заполненного списка продаж по дням недели дни с выручкой ниже средней'''
        array_titles_days_of_the_week_with_min_sales = [sales_lst_by_days_of_the_week[i - 1][0] for i in array_control_real_work_shop_by_days_of_the_week if sales_lst_by_days_of_the_week[i - 1][-1] < average_sales_by_day_of_the_week]
        '''выбираем из заполненного списка продаж по месяцам те месяца, где выручка ниже средней'''
        array_titles_months_with_min_sales = [sales_lst_by_months[i - 1][0] for i in array_control_real_work_shop_to_months if sales_lst_by_months[i - 1][-1] < average_number_of_sales_by_month]

        return f"Список дней недели с продажами выше или равными средним: {', '.join(array_titles_days_of_the_week_with_max_sales)}\n"\
               f"Список месяцев с продажами выше или равными средним: {', '.join(array_titles_months_with_max_sales)}\n"\
               f"Список дней недели с продажами ниже средних: {', '.join(array_titles_days_of_the_week_with_min_sales)}\n"\
               f"Список месяцев с продажами ниже средних: {', '.join(array_titles_months_with_min_sales)}"

#print(search_days_and_months_withs_max_sales_withs_high_speed_algorithm('data.csv'))


#______________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________

#2 вариант решения проблемы
def search_days_and_months_withs_max_sales_withs_low_speed_algorithm(file_name):
    '''
    функция собирает данные о продажах из электронной таблицы в формате 'csv',
    упковывает  их данные в двумерный список в формате: дата|кол_во продаж,
    исключая при этом дни недели и месяцы, когда магазин не работал (ввод некорректных данных)
    и выводит таблицы с продажами выше и ниже средних по неделям и месяцам
    :param file_name: date,visitors \n 2023-01-01,150  \n 2023-01-02,200 и т.д.
    :return: список дней недели с продажами выше среднего: вторник, суббота и т.д.
             список месяцев с продажами выше среднего: январь и т.д.
             список дней недели с продажами ниже среднего: средаЮ четверг и т.д.
             список месяцев с продажами ниже среднего: февраль и т.д.
    '''

    '''проверяем существует ли файл'''
    if os.path.exists(file_name) != True:
        raise FileNotFoundError('ИСКОМОГО ВАМИ ФАЙЛА НЕ СУЩЕСТВУЕТ !')

    sales_by_days_of_the_week = [0, 0, 0, 0, 0, 0, 0] #cоздаем список, в которым каждый эл_нт является счетчиком, который будет учитывать продажы по каждому из 7 дней недели
    sales_by_day_to_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #cоздаем список, в которым каждый эл_нт является счетчиком, который будет учитывать продажы по каждому из 12 месяцев
    total_sales = 0 # счетчик тотальных продаж за весь рассматриваемый период времен
    array_control_real_work_shop_by_days_of_the_week = set() #множество номеров недель, в которые магазин реально работал
    array_control_real_work_shop_to_months = set() #множество номеров месяцев, в которые магазин реально работал

    with open(file_name, encoding ='utf-8') as file:
        csv_reader = [i for i in csv.reader(file)] #преобразовываем входные данные в список для удобства обработки

        for row in csv_reader[1:]:


            if len(row) != 2: #обрабатываем исключение длины строки в формате: дата, кол_во продаж
                raise ValueError('НЕСООТВЕТСТВУЮЩАЯ ФОРМАТУ (ДАТА|КОЛ_ВО ПРОДАЖ) СТРОКА !')

            array_date = row[0].split('-') #преобразовываем информацию о датах в список

            if len(array_date) != 3: #обрабатываем исключение на соответствие формату даты
                raise ValueError('НЕСООТВЕТСТВУЮЩАЯ ФОРМАТУ (ГОД|МЕСЯЦ|ЧИСЛО) ДАТА ! ')

            #вычисляем дни недели дат в модуле дататайм и обрабатываем исключение на несуществующую дату
            try: date = datetime.datetime(int(array_date[0]), int(array_date[1]), int(array_date[2]))
            except: raise ValueError('УКАЗАНА НЕСУЩЕСТВУЮЩАЯ ДАТА !')

            #преобразоваваем данные о дневной выручке в тип данных |int| и обрабатываем исключения
            try: daily_sales = int(row[-1])
            except: raise ValueError('НЕВОЗМОЖНО ПРЕОБРАЗОВАТЬ ДАННЫЕ В ЧИСЛО !')

            sales_by_days_of_the_week[date.isoweekday() - 1] += daily_sales #заносим данные о продажах по каждому дню недели в список
            array_control_real_work_shop_by_days_of_the_week.add(date.isoweekday())  # заносим во множество номера днней недели в которые магазин работал

            sales_by_day_to_month[int(array_date[1]) - 1] += daily_sales #заносим данные о продажах по каждому месяцу в список
            array_control_real_work_shop_to_months.add(int(array_date[1])) #заносим во множество номера месяцев в которые магазтн работал

            total_sales += daily_sales #суммируем счетчик тотальных продаж

    average_sales_by_day_of_the_week = int(total_sales / len(array_control_real_work_shop_by_days_of_the_week)) #вычисляем среднее значение продаж по неделям
    average_number_of_sales_by_month = int(total_sales / len(array_control_real_work_shop_to_months)) #вычисляем среднее значение продаж по месяцам

    array_day_of_the_week = ['понедельник',
                             'вторник',
                             'cреда',
                             'четверг',
                             'пятница',
                             'cуббота',
                             'воскресенье'
                             ]

    array_months = ['январь',
                    'февраль',
                    'март',
                    'апрель',
                    'май',
                    'июнь',
                    'июль',
                    'август',
                    'сентябрь',
                    'октябрь',
                    'ноябрь',
                    'декабрь'
                    ]

    array_the_day_of_the_week_with_sales_more_average = [] #создаем список, который будет хранить номера дней недели с продажами выше среднего
    array_the_day_of_the_month_with_sales_more_average = [] #создаем список, который будет хранить номера месяцев с продажами выше среднего

    array_the_day_of_the_week_with_sales_less_average = []  # создаем список, который будет хранить номера дней недели с продажами выше среднего
    array_the_month_with_sales_less_average = []  # создаем список, который будет хранить номера месяцев с продажами выше среднего


    #находим мясяца и недели с продажами выше и ниже среднего
    for i in range(max(len(array_control_real_work_shop_by_days_of_the_week), len(array_control_real_work_shop_to_months))):

        try:
            if i+1 in array_control_real_work_shop_by_days_of_the_week: #проверяем работал ли магазин в данный день недели
                if sales_by_days_of_the_week[i] >= average_sales_by_day_of_the_week:
                    #если уровень продаж в данный день недели выше среднего- заносим номер дня недели в список с высоким уровнем понедельных продаж
                    array_the_day_of_the_week_with_sales_more_average.append(i)
                if sales_by_days_of_the_week[i] < average_sales_by_day_of_the_week:
                    # если уровень продаж в данный день недели ниже среднего- заносим номер недели в список с низким уровнем понедельных продаж
                    array_the_day_of_the_week_with_sales_less_average.append(i)

            if i+1 in array_control_real_work_shop_to_months: #проверяем, работал ли магазин в данный месяц
                # если уровень продаж в данный месяц выше среднего- заносим номер месяца в список с высоким уровнем помесячных продаж
                if sales_by_day_to_month[i] > average_number_of_sales_by_month:
                    array_the_day_of_the_month_with_sales_more_average.append(i)
                # если уровень продаж в данный месяц ниже среднего- заносим номер месяца в список с низким уровнем помесячных продаж
                if sales_by_day_to_month[i] < average_number_of_sales_by_month:
                    array_the_month_with_sales_less_average.append(i)

        except: continue #исключаем ошибку в расчетах т.к. длины списков кол_ва месяцев в году и кол_ва дней в неделе различны

    #Cоздаем список дней недели по названиям в порядке возрастания с максимальным уровнем продаж
    array_titles_days_of_the_week_with_max_sales = [array_day_of_the_week[i] for i in range(len(array_day_of_the_week)) if i in array_the_day_of_the_week_with_sales_more_average]
    # Cоздаем список месяцев по названиям в порядке возрастания с максимальным уровнем продаж
    array_titles_months_with_max_sales = [array_months[i] for i in range(len(array_months)) if i in array_the_day_of_the_month_with_sales_more_average]

    # Cоздаем список дней недели по названиям в порядке возрастания с минимальным уровнем продаж
    array_titles_days_of_the_week_with_min_sales = [array_day_of_the_week[i] for i in range(len(array_day_of_the_week)) if i in array_the_day_of_the_week_with_sales_less_average]
    # Cоздаем список месяцев по названиям в порядке возрастания с минимальным уровнем продаж
    array_titles_months_with_min_sales = [array_months[i] for i in range(len(array_months)) if i in array_the_month_with_sales_less_average]



    return  f'Список дней недели с продажами выше среднего: {", ".join(array_titles_days_of_the_week_with_max_sales)}\n' \
            f'Список месяцев с продажами выше среднего: {", ".join(array_titles_months_with_max_sales)}\n'\
            f'Список дней недели с продажами ниже среднего: {", ".join(array_titles_days_of_the_week_with_min_sales)}\n' \
            f'Список месяцев с продажами ниже среднего: {", ".join(array_titles_months_with_min_sales)}'


#print(search_days_and_months_withs_max_sales_withs_low_speed_algorithm('data.csv'))
