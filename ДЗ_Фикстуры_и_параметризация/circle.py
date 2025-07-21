from decimal import Decimal
class Circle:

    def __init__(self, r):
        self.__r = self.__correct_input_data_r(r)
        self.pi = Decimal(3.14)

    def __correct_input_data_r(self, r):
        if not isinstance(r, (int, float)):
            raise ValueError('Тип входных данных должен быть только: int|float  !')
        if r <= 0:
            raise ValueError('Значение радиуса должно быть больше нуля!')
        return r

    def area(self):
        """
        Возвращается площадь окружности
        r = 5
        area = 3.14 * (5**2)
        return: 78.5
        """
        r = float(self.pi * Decimal(self.__r) ** 2)
        return round(r, 2)

    def circumference(self):
        """
        Возвращается длина окружности
        r = 5
        circumference = 2 * 3.14 * 5
        return: 31.4
        """
        r = float(2 * self.pi * Decimal(self.__r))
        return round(r, 2)

    def diameter(self):
        """
        Возвращается диаметр окружности
        r = 5
        diameter = 2 * 5
        :return: 10
        """
        return round(int(2 * Decimal(self.__r)), 2)

    def get_r(self):
        """
        Возвращается значение радиуса окружности
        return: r
        """
        return self.__r

    def set_r(self, new_r):
        """
        Устанавливается новое значение радиуса окружности
        """
        self.__r = self.__correct_input_data_r(new_r)

    def __repr__(self):
        return f'РАДИУС ОКРУЖНОСТИ: {self.__r}'

c = Circle(3)
print(c)
print(f'Площадь окружности диаметром = {c.get_r()}: {c.area()}')
c.set_r(5)
print(f'Площадь окружности диаметром = {c.get_r()}: {c.area()}')
print(c.circumference())