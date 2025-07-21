from decimal import Decimal
import math
import random

class Vector:

    def __init__(self, x: (int,float), y: (int,float), z: (int,float)):
        if self.__correct_input_data(x)==self.__correct_input_data(y)==self.__correct_input_data(z)==0:
            raise ValueError('Невозможно существование вектора, где все координаты равны нулю')
        self.__x = self.__correct_input_data(x)
        self.__y = self.__correct_input_data(y)
        self.__z = self.__correct_input_data(z)


    def __correct_input_data(self,data):
        if not isinstance(data,(int, float)):
            raise TypeError('Тип входных данных должен быть только: int|float  !')
        return data


    def get_x(self):
        """
        Возвращается значение координаты 'x'
        return: X
        """
        return self.__x

    def set_x(self,new_x):
        """
        Устанавливается новое значение координаты 'x'
        """
        self.__x = self.__correct_input_data(new_x)

    def get_y(self):
        """
        Возвращается значение координаты 'y'
        return: y
        """
        return self.__y

    def set_y(self, new_y):
        """
        Устанавливается новое значение координаты 'y'
        """
        self.__y = self.__correct_input_data(new_y)

    def get_z(self):
        """
        Возвращается значение координаты 'z'
        return: z
        """
        return self.__z

    def set_z(self, new_z):
        """
        Устанавливаетя новое значение координаты 'z'
        """
        self.__z = self.__correct_input_data(new_z)

    def length(self):
        """
        Возвращается длину вектора
        a(1,2,3)
        lenght_vector = (1**2 + 2**2 + 3**2)**0.5 = 3.74
        return: lenght_vector
        """
        result = (Decimal(self.__x) ** 2 + Decimal(self.__y) ** 2 + Decimal(self.__z) ** 2) ** Decimal(0.5)
        lenght_vector = round(float(result), 2)
        return lenght_vector

    def add(self, other: 'Vector'):
        """
        Возвращается сумма текущего и  нового вектора
        v1(1,1,1)
        v2(2,2,2)
        v3 = v1(1,1,1) + v2(2,2,2)
        :return: v3
        """
        x = round(float(Decimal(self.__x) + Decimal(other.__x)), 2)
        y = round(float(Decimal(self.__y) + Decimal(other.__y)), 2)
        z = round(float(Decimal(self.__z) + Decimal(other.__z)), 2)
        return Vector(x, y, z)

    def sub(self, other: 'Vector'):
        """
        Возвращается разница текущего и  нового вектора
        v1(3,3,3)
        v2(2,2,2)
        v3 = v1(3,3,3) - v2(2,2,2)
        :return: v3
        """
        x = round(float(Decimal(self.__x) - Decimal(other.__x)), 2)
        y = round(float(Decimal(self.__y) - Decimal(other.__y)), 2)
        z = round(float(Decimal(self.__z) - Decimal(other.__z)), 2)
        return Vector(x, y, z)

    def scalar_mul(self, other: 'Vector'):
        """
        Возвращается скалярное произведение текущего и нового вектора
        v1(2,2,2)
        v2(3,3,3)
        v3 = v1(2,2,2) * v2(3,3,3)
        return: v3
        """
        x = Decimal(self.__x) * Decimal(other.__x)
        y = Decimal(self.__y) * Decimal(other.__y)
        z = Decimal(self.__z) * Decimal(other.__z)
        return round(float(x + y + z), 2)

    def angle_between(self, other: 'Vector'):
        """
        Возвращается угол в радианах между текущим и новым вектором
        v1(1,1,1)
        v2(2,2,2)
        произведение_v1_&_v2: (1*2 + 1*2 + 1*2) = 6
        длина_v1 = (1*1 + 1*1 + 1*1)**0.5=1.73
        длина_v2 = (2*2 + 2*2 + 2*2)**0.5=3.46
        косинус_v1_&_v2:  6 / (1.73*3.46)=1.0023
        радианы: arccos(косинус_v1_&_v2)=0.22
        return: радианы
        """
        scalar_mull_v1_and_v2 = Decimal(self.scalar_mul(other))
        length_v1 = Decimal(self.length())
        length_v2 = Decimal(other.length())
        cos_corner = scalar_mull_v1_and_v2 / (length_v1 * length_v2)
        rad_corner = round(float(math.acos(cos_corner)), 2)
        return rad_corner

    @staticmethod
    def random_int(min_d,max_d):
        """
        Создается вектор из диапазона случайных значений (int)
        v.(рандом в диапазоне: 0,5)
        return: V(1,3,2)
        """
        x = random.randint(min_d, max_d)
        y = random.randint(min_d, max_d)
        z = random.randint(min_d, max_d)
        return Vector(x, y, z)

    @staticmethod
    def random_float(min_d, max_d):
        """
        Создается вектор из диапазона случайных значений (float)
        v.(рандом в диапазоне: 0.5, 10.5)
        return: V(0.5, 3.2, 2.4)
        """
        x = random.uniform(min_d, max_d)
        y = random.uniform(min_d, max_d)
        z = random.uniform(min_d, max_d)
        return Vector(x, y, z)

    def __repr__(self):
        return f'{self.__x}, {self.__y}, {self.__z}'

v1=Vector(1,2,3)
v2 = Vector(4, 5, 6)
print(v1.length())
print(v2.length())
print(v1.add(v2))
print(v1.angle_between(v2))
v3=Vector.random_int(1,10)
print(v3)
v4=Vector.random_float(0.2, 12.5)
print(v4)