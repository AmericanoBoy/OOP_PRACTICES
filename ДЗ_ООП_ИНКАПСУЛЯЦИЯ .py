
#ЗАДАНИЕ №1

from __future__ import annotations

class BankAccount:
    def __init__(self, owner: str, balance: float):
        if not isinstance(owner, str):
            raise ValueError('Имя должно быть строкой')
        self.__owner = owner
        if balance < 0 if isinstance(balance, (int, float)) else not isinstance(balance, (int, float)):
            raise ValueError('Баланс не может быть меньше нуля или строкой')
        self.__balance = balance

    def get_owner(self):
        return f'Клиент: {self.__owner}'

    def set_owner(self, new_owner: str):
        if not isinstance(new_owner, str):
            raise TypeError("Данные клиента должны быть строкой")
        self.__owner = new_owner

    def get_balance(self):
        return f'Состояние счета клиента: {float(self.__balance)}'

    def set_balance(self, new_balance: str or float):
        if new_balance < 0 if isinstance(new_balance, (int, float)) else not isinstance(new_balance, (int, float)):
            raise ValueError('Баланс не может быть меньше нуля или строкой')
        self.__balance = new_balance

    def __repr__(self):
        return BankAccount(self.__owner, self.__balance__b)


b=BankAccount('Богачев Вася',1000)
print(b.get_owner())
b.set_owner('Бедняков Петя')
print(b.get_owner())
print(b.get_balance())
b.set_balance(10)
print(b.get_balance())

#__________________________________________________________________________________________________________________________________________________________________________

#ЗАДАНИЕ №2

from __future__ import annotations

class Rectangle:
    def __init__(self, width: int or float, height: int or float):
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError('высота прямоугольнька должнна быть числом больше нуля')
        self.__height = height
        if not isinstance(width, (int, float)) or width <0:
            raise ValueError('ширина прямоугольнька должнна быть числом больше нуля')
        self.__width = width

    def get_width(self):
        return f'Ширина прямоугольника: {float(self.__width)}'

    def set_width(self, new_width: float):
        if new_width < 0 if isinstance(new_width, (float, int)) else not isinstance(new_width, (float, int)):
            raise ValueError("Тип данных ширины прямоуголника должен быть цифрой больше нуля")
        self.__width = new_width

    def get_height(self):
        return f'Высота прямоуггольника: {float(self.__height)}'

    def set_height(self, new_height: int or float):
        if isinstance(new_height, (int, float)) and new_height > 0:
            self.__height = new_height
        else:
            raise ValueError("Тип данных высоты прямоуголника должен быть цифрой больше нуля")

    def area_rectangle(self):
        area_rectangle = self.__width * self.__height
        return float(area_rectangle)

    def __repr__(self):
        return Rectangle(self.__width, self.__height)



r=Rectangle(10,2)
print(r.get_width())
r.set_width(3)
print(r.get_width())
print(r.get_height())
r.set_height(10)
print(r.get_height())
print('Площадь прямоугольника:', r.area_rectangle())

#_________________________________________________________________________________________________________________________________________________________________________

#ЗАДАНИЕ №3

from __future__ import annotations

class Student:
    def __init__(self, name: str, grades: list):
        self.__name = name if isinstance(name, str) else ValueError('Имя должно быть строкой')
        self.__grades = grades if isinstance(grades, list) and sum([1 <= i <= 5 for i in grades if type(i) in [int, float]])==len(grades) else ValueError('Неверный ввод')

    def get_name(self):
        return f'Имя студента: {self.__name}'

    def set_name(self, new_name):
        self.__name = new_name if isinstance(new_name, str) else ValueError('Имя должно быть строкой')

    def get_grades(self):
        return f'Список оценок: {self.__grades}'

    def set_grades(self, new_grades):
        self.__grades = new_grades if isinstance(new_grades, list) and sum(1 <= i <= 5 for i in new_grades if type(i) in [int, float])==len(new_grades) else ValueError('Неверный ввод')

    def grades_averages(self):
        try: return f'Cредняя оценка {self.__name}: {round((sum(self.__grades)/len(self.__grades)),2)}'
        except: return 'Неверный ввод'

    def __repr__(self):
        return Student(self.__name, self.__grades)


s=Student('Вася Двоечечников', [2, 3, 3, 3, 2])
print(s.get_name())
print(s.get_grades())
print(s.grades_averages())

#__________________________________________________________________________________________________________________________________________________________________________

#ЗАДАНИЕ №4

from __future__ import annotations

class TemperatureLog:
    def __init__(self, city: str, lst_temperatures: list):
        self.__city = city if isinstance(city, str) else ValueError('Название города должно быть строкой')
        self.__lst_temperatures = lst_temperatures if isinstance(lst_temperatures, list) and sum(-100 <= i <= 90 for i in lst_temperatures if type(i) in [int, float]) == 7 else ValueError('Неверный ввод')

    def get_city(self):
        return f'Город: {self.__city}'

    def set_city(self, new_city):
        self.__city = new_city if isinstance(new_city, str) else ValueError('Название города должно быть строкой')

    def get_lst_temperatures(self):
        return f'Список температуры за неделю: {self.__lst_temperatures}'

    def set_lst_temperatures(self, new_lst_temperatures):
        self.__lst_temperatures = new_lst_temperatures if isinstance(new_lst_temperatures, list) and sum(
            -100 <= i <= 90 for i in new_lst_temperatures if type(i) in [int, float]) == 7 else ValueError('Неверный ввод')

    def grades_averages(self):
        try: return f'Cредняя температура в {self.__city} за неделю: {round((sum(self.__lst_temperatures)/len(self.__lst_temperatures)),2)}'
        except: return 'Введены неверные данные'

    def max_temperature(self):
        try: return f'Максимальная температура в {self.__city} за неделю: {max(self.__lst_temperatures)}'
        except: return 'Введены неверные данные'

    def min_temperature(self):
        try: return f'Минималная температура в {self.__city} за неделю: {min(self.__lst_temperatures)}'
        except: return 'Введены неверные данные'

    def __repr__(self):
        return Student(self.__city, self.__lst_temperatures)

t=TemperatureLog('Улан-Батор', [22, 23, 25, 28, 29, 31, 28])
print(t.get_city())
print(t.get_lst_temperatures())
print(t.set_lst_temperatures([21, 23, 21, 20, 19, 18, 17]))

#__________________________________________________________________________________________________________________________________________________________________________

#ЗАДАНИЕ №5

from __future__ import annotations

class EmployeePayroll:

    def __init__(self, name: str, salary: float, tax_rate: float):
        self.__name = name if isinstance(name, str) else ValueError('Имя сотрудника должно быть строкой')
        self.__salary = [ValueError('З/П сотрудника должна быть больше нуля'), float(salary) ][salary > 0] if isinstance(salary, (int, float)) else ValueError('З/П должна быть числом')
        self.__tax_rate = [ValueError('Налог должен быть в диапазоне от 0 до 1'), tax_rate][0 < tax_rate < 1] if isinstance(tax_rate, float) else ValueError('Налога  должен быть дробным числом')

    def get_name(self):
        return f'Сотрудник: {self.__name}'

    def set_name(self, new_name):
        self.__name = new_name if isinstance(new_name, str) else ValueError('Имя сотрудника должно быть строкой')

    def get_salary(self):
        return f'Зарплата сотрудника: {self.__salary}'

    def set_salary(self, new_salary):
        uncorrect_input = ValueError('Зарплата сотрудника должна быть числом больше нуля')
        self.__salary = [uncorrect_input, new_salary][float(new_salary)>0] if isinstance(new_salary, (int, float)) else uncorrect_input

    def get_tax_rate(self):
        return f'{self.__name}. Величина налога: {self.__tax_rate}.'

    def set_tax_rate(self, new_tax_rate):
        uncorrect_input = ValueError('Величина налога должна быть дробным числом от нуля до единицы')
        self.__tax_rate = [uncorrect_input, new_tax_rate][0 < float(new_tax_rate) < 1] if isinstance(new_tax_rate, float) else uncorrect_input

    def net_salary(self):
        try: return f'З/П после вычета налогов: {self.__salary - (self.__tax_rate * self.__salary)}'
        except: return ValueError('Неверные данные для вычисления месячной З/П')

    def annual_net(self):
        try: return  f'З/П за год после вычета налогов: {12 * (self.__salary - (self.__tax_rate * self.__salary))}'
        except: return ValueError('Неверные данные для вычисления годовой З/П')

    def __repr__(self):
        return f'Имя: {self.__name}. З/П до налога: {self.__salary}. Налог: {self.__tax_rate}'

e=EmployeePayroll('Петр Простаков', 1000, 0.7 )
print(e.get_name())
print(e.get_salary())
print(e.get_tax_rate())
print(e.net_salary())
e.set_name('Иван Продуманов')
e.set_salary(12000)
e.set_tax_rate(0.1)
print(e.get_name())
print(e.get_salary())
print(e.get_tax_rate())
print(e.annual_net())
print(e)

#__________________________________________________________________________________________________________________________________________________________________________