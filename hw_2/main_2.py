#ЗАДАНИЕ № 1

from __future__ import annotations

class  Vector:
    def __init__(self, x:int = 0,y:int = 0):
        self.x = x
        self.y = y

    def add(self, other: Vector):
        return Vector(self.x + other.x, self.y + other.y)

    def sub(self, other: Vector):
        return Vector(self.x - other.x, self.y - other.y)

    def mul(self, scalar):
        return Vector(self.x * scalar,self.y * scalar)

    def __str__(self):
        return f"{self.x}, {self.y}"

v1=Vector(20,22)
v2=Vector(2,90)
print(v1)
print(v2)
v3=v1.add(v2)
print(v3)


#_________________________________________________________________________________________________________________________________________________________________________

#ЗАДАНИЕ № 2

#1 вариант решения
#-------------------------

from __future__ import annotations

class Money:
    def __init__(self, a:int,b:int):
        self.a = a
        self.b = b
        self.result = self.a*100 + self.b

    def add(self,other:Money):
        result = self.result + other.result
        return f'Dollar:{result//100},Cent:{result%100}'

    def sub(self,other:Money):
        result = self.result - other.result
        return f'Dollar:{result//100},Cent:{result%100}'

    def __repr__(self):
        return f'Dollar:{self.result//100},Cent:{self.result%100}'

t1=Money(20,22)
t2=Money(2,90)
print(t1)
print(t2)
t3=t1.add(t2)
t4=t2.sub(t1)
print(repr(t4))


#2 вариант решения
#-------------------------
from __future__ import annotations

class Money:
    def __init__(self, a:int,b:int):
        self.a = a
        self.b = b

    def add(self,other:Money):
        a = self.a + other.a
        b = self.b + other.b
        return f'Dollar:{a+b//100},Cent:{b%100}'

    def sub(self,other:Money):
        a = self.a - other.a
        b = self.b - other.b
        return f'Dollar:{a+b//100},Cent:{b%100}'

    def __repr__(self):
        return f'Dollar:{self.a+self.b//100},Cent:{self.b%100}'

t1=Money(20,22)
t2=Money(2,90)
print(t1)
print(t2)
t3=t1.add(t2)
t4=t2.sub(t1)
print(repr(t4))


#_________________________________________________________________________________________________________________________________________________________________________

#ЗАДАНИЕ № 3

from __future__ import annotations

class Time:
    def __init__(self, hours:int, minutes: int, seconds:int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add(self, other: Time):
        hours = other.hours + self.hours
        minutes = other.minutes + self.minutes
        seconds = other.seconds + self.seconds
        seconds_copy = seconds
        seconds = seconds % 60
        minutes_copy = minutes
        minutes = (minutes + seconds_copy//60)%60
        hours = minutes_copy//60+hours
        return Time(hours,minutes,seconds)

    def len(self):
        return f'Общее кол_во секунд: {self.hours*3600 + self.minutes*60 + self.seconds}'

    def __repr__(self):
        return f'Time: {self.hours} h,{self.minutes} min,{self.seconds} sec.'

t1=Time(1,52,50)
t2=Time(2,40,40)
print(t1)
t3=t1.add(t2)
print(t3)
print(t3.len())

#_________________________________________________________________________________________________________________________________________________________________________

 #ЗАДАНИЕ №4

from __future__ import annotations

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add(self, other: Point):
        x, y = self.x + other.x, self.y + other.y
        return Point(x, y)

    def sub(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return Point(self.x, self.y)

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

#_________________________________________________________________________________________________________________________________________________________________________

#ЗАДАНИЕ №5

class Coloredpoint(Point):
    def __init__(self, x, y, color:str):
        super().__init__(x, y)
        self.color = color

    def add(self,other: Coloredpoint):
        x, y = self.x + other.x, self.y + other.y
        color = ['black', self.color][other.color == self.color]
        return Coloredpoint(x, y, color)

    def sub(self,other: Coloredpoint):
        x, y = self.x - other.x, self.y - other.y
        color = ['black', self.color][other.color == self.color]
        return Coloredpoint(x,y,color)

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, color: {self.color}"

p1=Coloredpoint(1,2,'e')
p2=Coloredpoint(2,3,'w')
print(p1.add(p2))
print(p1.sub(p2))


#_________________________________________________________________________________________________________________________________________________________________________

#ЗАДАНИЕ № 6

#1вариант решения:

from __future__ import annotations

import random

class Matrix:
    def __init__(self, a:int,b:int):
        self.a = a
        self.b = b
        self.mat=[[random.randint(1, 5) for i in range(a)] for j in range(b)]

    def add(self,other:Matrix):
        result_mat = Matrix(self.a,self.b)
        for i in range(self.a):
            for j in range(self.b):
                result_mat.mat[i][j] = self.mat[i][j]+other.mat[i][j]
        return result_mat

    def mul(self, other:Matrix):
        result_mat = Matrix(self.a, self.b)
        for i in range(self.a):
            for j in range(self.b):
                result_mat.mat[i][j] = self.mat[i][j] * other.mat[i][j]
        return result_mat

    def mul_some_number(self,number):
        result_mat = Matrix(self.a, self.b)
        for i in range(self.a):
            for j in range(self.b):
                result_mat.mat[i][j] = self.mat[i][j] * number
        return result_mat

    def calculation_len_matrix(self):
        count = 0
        for i in range(self.a):
            for j in range(self.b):
                count += 1
        return count

    def __repr__(self):
        return f'{self.mat}'

t1=Matrix(2,2)
t2=Matrix(2,2)
print(t1)
print(t2)
t3=t1.add(t2)
print(t3)
t4=t1.mul(t2)
print(t4)
print(t1.mul_some_number(5))

#-------------------------------------------
#2 вариант решения:

from __future__ import annotations

class Matrix:
    def __init__(self, a:int,b:int,c:int,d:int,mat:list):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.mat = mat

    def create_matrix(self):
        temp=[]
        c = 2
        for el in [self.a, self.b, self.c, self.d]:
            temp.append(el)
            if len(temp) == c:
                self.mat.append(temp)
                temp = []
        return self.mat

    def add(self,other:Matrix):
        z=[]
        q=[]
        for i in range(2):
            for j in range(2):
                q.append(self.mat[i][j]+other.mat[i][j])
            z.append(q)
            q = []
        return z

    def mul(self,other:Matrix):
        z=[]
        q=[]
        for i in range(2):
            for j in range(2):
                q.append(self.mat[i][j]*other.mat[i][j])
            z.append(q)
            q = []
        return z

    def mul_some_number(self,number):
        z = []
        q = []
        for i in range(2):
            for j in range(2):
                q.append(self.mat[i][j] * number)
            z.append(q)
            q = []
        return z

    def calculation_len_matrix(self):
        count = 0
        for i in range(2):
            for j in range(2):
                count += 1
        return count

    def __repr__(self):
        return f'{self.mat}'

t1=Matrix(1,2,3,4,[])
t2=Matrix(1,2,3,4,[])
print(t1.create_matrix())
print(t2.create_matrix())
t3=t1.add(t2)
print(t3)
t4=t1.mul(t2)
print(t4)
print(t1.mul_some_number(5))



#__________________________________________________________________________________________________________________________________________________________________________

#ЗАДАНИЕ № 7

from __future__ import annotations

class Temperature:
    def __init__(self, degrees:int):
        if degrees<-273:
            self.degrees = -273
        else:
            self.degrees = degrees

    def add(self, other: Temperature):
        degrees = other.degrees + self.degrees
        return Temperature(degrees)

    def sub(self, other: Temperature):
        degrees = other.degrees - self.degrees
        return Temperature(degrees)

    def mul(self,factor):
        return f'{self.degrees}+{factor}={self.degrees+factor}'

    def __repr__(self):
        return f'Temperature: {self.degrees}  C.'

t1=Temperature(int(input('введите значение температуры:  ')))
t2=Temperature(int(input('введите значение температуры:  ')))
print(t1)
t3=t1.add(t2)
print(t3.mul(5))

#__________________________________________________________________________________________________________________________________________________________________________


