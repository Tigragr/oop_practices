from __future__ import annotations

#Задача_1
print()
print("\u001b[33mЗадача_1_>>>>>>>>>>>\u001b[0m")

class Wizard:

    name: str
    house: str
    force: int
    spells: list
    status: bool

    def __init__(self,name,house,force,spells = None,status = None):

        self.__name = name
        self.__house = house
        self.__force = force
        self.__spells = spells or []
        self.__status = status or False

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_force(self):
        return self.__force

    def get_spells(self):
        return self.__spells

    def get_status(self):
        return self.__status

    def set_house(self,house):
        self.__house = house

    def set_force(self,force):
        self.__force = force if force >= 0 else self.__force

    def set_status(self,status):
        self.__status = status
###################################################
###################################################
    def add_spell(self, new_spell:Spell): # добавляет заклинание в список известных.
        if new_spell not in self.spells:
            self.__spells.append(new_spell)

    def remove_spell(self, del_spell: Spell): # удаляет заклинание из списка известных.
        if del_spell in self.spells:
            self.__spells.remove(del_spell)

    def increase_force(self, amount: int): # увеличивает уровень магической силы на заданное значение (неотрицательное).
        increase = amount if amount >= 0 else 0
        self.force = self.force + increase

    def __str__(self):
        return self.name,self.house,self.force,self.spells,self.status

###################################################
###################################################

class Spell:

    name: str
    difficulty: int
    type: str

    def __init__(self, name, difficulty, type):
        self.__name = name
        self.__difficulty = difficulty
        self.__type = type

    def get_name(self):
        return self.__name

    def get_difficulty(self):
        return self.__difficulty

    def get_type(self):
        return self.__type

























class Patient:

    def __init__(self, name: str ="Не задано", age: int = 0, disease: str = "Не задано"):
        self.__name = name
        self.__age = age
        self.__disease = disease

    def __set_name(self, new_name):
        self.__name = new_name

    def __get_name(self):
        return self.__name

    def __set_age(self, new_age):
        self.__age = new_age

    def __get_age(self):
        return self.__age

    def __set_disease(self, new_disease):
        self.__disease = new_disease

    def __get_disease(self):
        return self.__disease

    def appointment(self, date: str, time: str):
        self.about_patient()
        print("Время записи:", date + " " + time)

    def about_patient(self):
        print("Пациент:", self.__name, "\n",
              "Возраст:", self.__age, "\n",
              "Болезнь:", self.__disease)

    name = property(__get_name,__set_name)
    age = property(__get_age,__set_age)
    disease = property(__get_disease, __set_disease)

p = Patient()
p.name = "Вася"
p.age = 18
p.disease = "Энурез"
p.appointment("Дата", "Время")


#Задача_2
print()
print("\u001b[33mЗадача_2_>>>>>>>>>>>\u001b[0m")

class TouristSpot:
    def __init__(self, place: str, land: str, type_showplace: str):
        self.__place = place
        self.__land = land
        self.__type_showplace = type_showplace

    def __get_place(self):
        return self.__place

    def __set_place(self, new_place):
        self.__place = new_place

    def __get_land(self):
        return self.__land

    def __set_land(self, new_land):
        self.__land = new_land

    def __get_type_showplace(self):
        return self.__place

    def __set_type_showplace(self, new_type_showplace):
        self.__type_showplace = new_type_showplace

    def goPlace(self, name_tourist: str):
        print(f"Tурист {name_tourist} посетил достопримечательность {self.__place}, относящуюся к типу '{self.__type_showplace}' в стране {self.__land}")
        return ""

    def info(self):
        print(f"Название достопримечательности: {self.__place}\nТип достопримечательности: {self.__type_showplace}\nСтрана: {self.__land}")
        return ""

    place = property(__get_place,__set_place)
    land = property(__get_land,__set_land)
    type_showplace = property(__get_type_showplace,__set_type_showplace)

ts = TouristSpot("Кремль","Россия","Исторический")
print(ts.info())
ts.place = "Байкал"
ts.type_showplace = "Природный"
print(ts.goPlace("Петя"))


#Задача_3
print()
print("\u001b[33mЗадача_3_>>>>>>>>>>>\u001b[0m")

class ModelWindow:

    __max_x = 1960
    __min_x = 0
    __max_y = 1080
    __min_y = 0

    title: str
    coord_start: list
    size_h: int
    size_v: int
    color_window: str
    is_visibal: bool
    is_bord: bool

    def __init__(self, title = "ЗАГОЛОВОК", coord_start = [50,50], size_h = 100, size_v = 150, color_window = "Red", is_visibal = True, is_bord = True):
        self.__title = title
        self.__coord_start = coord_start
        self.__size_h = size_h
        self.__size_v = size_v
        self.__color_window = color_window
        self.__is_visibal = is_visibal
        self.__is_bord = is_bord

    def move_window(self, new_coord_start):
        if new_coord_start[0] >= ModelWindow.__max_x:
            self.__coord_start[0] = ModelWindow.__max_x
        elif new_coord_start[0] <= ModelWindow.__min_x:
            self.__coord_start[0] = ModelWindow.__min_x
        else:
            self.__coord_start[0] = new_coord_start[0]

        if new_coord_start[1] >= ModelWindow.__max_y:
            self.__coord_start[1] = ModelWindow.__max_y
        elif new_coord_start[1] <= ModelWindow.__min_y:
            self.__coord_start[1] = ModelWindow.__min_y
        else:
            self.__coord_start[0] = new_coord_start[0]

    def resize_window(self, change_size_h, change_size_v):
        if self.__coord_start[0] + change_size_h >= ModelWindow.__max_x:
            self.__size_h = ModelWindow.__max_x - self.__coord_start[0]
        if change_size_h <= ModelWindow.__min_x:
            self.__size_h = 1
        else:
            self.__size_h += change_size_h


        if self.__coord_start[1] + change_size_v >= ModelWindow.__max_y:
            self.__size_v = ModelWindow.__max_y - self.__coord_start[1]
        if change_size_v <= ModelWindow.__min_y:
            self.__size_v = 1
        else:
            self.__size_v += change_size_v

    def change_color(self, new_color):
        self.color = new_color

    def vision(self, new_visibal):
        self.__is_visibal = new_visibal
        vis = "Окно видимо" if self.__is_visibal else "Окно не видимо"
        print(vis)

    def __str__(self):
        str_top_window = str(self.__title)
        str_coord_start = f"[{self.__coord_start[0]}, {self.__coord_start[1]}]"
        str_size_h = str(self.__size_h)
        str_size_v = str(self.__size_v)
        str_color_w = str(self.__color_window)
        str_is_visibal = str(self.__is_visibal)
        str_is_bord = str(self.__is_bord)
        print(f"Заголовок окна: {str_top_window},\n"
              f"Координаты верхнего левого угла окна: {str_coord_start},\n"
              f"Ширина окна: {str_size_h},\nВысота окна: {str_size_v},\n"
              f"Цвет окна: {str_color_w},\nВидимость окна: {str_is_visibal},\nВидимость границ: {str_is_bord}")

ModelWindow().__str__()


#Задача_4
print()
print("\u001b[33mЗадача_4_>>>>>>>>>>>\u001b[0m")

class ArrayUtils:
    @staticmethod
    def summa(lst: list) -> int:

        res = 0
        for el in lst:
            res += el

        return res

    @staticmethod
    def multipl(lst: list) -> int:

        res = 1
        for el in lst:
            res *= el

        return res

    @staticmethod
    def invers_list(lst: list) -> list:

        res = []
        for el in lst:
            res.insert(0,el)

        return res

    @staticmethod
    def max_element(lst: list) -> int:

        max_el = lst[0]
        for el in lst:
            if el > max_el:
                max_el = el

        return max_el

    @staticmethod
    def min_element(lst: list) -> int:

        min_el = lst[0]
        for el in lst:
            if el < min_el:
                min_el = el

        return min_el

l = [3,2,1,4,5,9,4,2]
a = ArrayUtils()

print(a.invers_list(l),a.max_element(l),a.min_element(l),a.summa(l),a.multipl(l))


#Задача_5
print()
print("\u001b[33mЗадача_5_>>>>>>>>>>>\u001b[0m")

class Vector:

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z

        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z

        return Vector(new_x, new_y, new_z)

    def __mul__(self, other):
        if type(other).__name__ == "int" or type(other).__name__ == "float":
            new_x = self.x * other
            new_y = self.y * other
            new_z = self.z * other
        else:
            new_x = self.z * other.y - self.y * other.z
            new_y = self.x * other.z - self.z * other.x
            new_z = self.y * other.x - self.x * other.y

        return Vector(new_x, new_y, new_z)

    def norma(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** 1/2

    def __str__(self):
        return f'Результат операции: "{self.x,self.y,self.z}"'

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)

vv = v1 + v2
vvv = v1 * 2
vvvv = v1 * v2

print(vv)
print(vvv)
print(vvvv)


#Задача_6
print()
print("\u001b[33mЗадача_6_>>>>>>>>>>>\u001b[0m")

class Fraction:

    @staticmethod
    def checkZeroDenom(denom: int) -> bool:
        if denom == 0:
            print("Знаменатель равен нулю. Вычисление невозможно.")
            res = False
        else:
            res = True
        return res

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self,other):

        if Fraction.checkZeroDenom(self.denominator) == False or Fraction.checkZeroDenom(other.denominator) == False:
            return ''

        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator,new_denominator)

    def __mul__(self, other):

        if Fraction.checkZeroDenom(self.denominator) == False or Fraction.checkZeroDenom(other.denominator) == False:
            return ''

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)


    def __sub__(self, other):

        if Fraction.checkZeroDenom(self.denominator) == False or Fraction.checkZeroDenom(other.denominator) == False:
            return ''

        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __str__(self):

        less = abs(self.denominator) if abs(self.denominator) < abs(self.numerator) else abs(self.numerator)
        for i in range(less, 0, -1):

            if self.denominator % i != 0 or self.numerator % i != 0:
                continue

            self.numerator = self.numerator / i
            self.denominator = self.denominator / i
            break

        if self.denominator == 1:
            res = str(int(self.numerator))
        else:
            res = str(int(self.numerator)) + "/" + str(int(self.denominator))

        return "Результат операции: " + res

d1 = Fraction(128,358)
d2 = Fraction(15,25)
print("d1 + d2 -> ", d1+d2)
print("d1 * d2 -> ", d1*d2)
print("d1 - d2 -> ", d1-d2)


#Задача_7
print()
print("\u001b[33mЗадача_7_>>>>>>>>>>>\u001b[0m")

import math
class GeometryUtils:

    @staticmethod
    def areaCircle(radius: float) -> float:
        return math.pi * radius ** 2

    @staticmethod
    def perimeterCircle(radius: float) -> float:
        return math.pi * radius * 2

    @staticmethod
    def areaRectangle(length: float, width: float) -> float:
        return length * width

    @staticmethod
    def perimeterRectangle(length: float, width: float) -> float:
        return 2 * (length + width)

    @staticmethod
    def areaTriangle(side_1: float, side_2: float, side_3: float) -> float:
        p = (side_1 + side_2 + side_3) / 2
        if (p - side_1 > 0 and p - side_2 > 0 and p - side_3 > 0):
            return math.sqrt(p * (p - side_1) * (p - side_2) * (p - side_3))
        else:
            print("Треугольник с такими сторонами не существует.")
            return ''

print(GeometryUtils.areaTriangle(1,3,1))
print(GeometryUtils.areaTriangle(3,4,5))


#Задача_8
print()
print("\u001b[33mЗадача_8_>>>>>>>>>>>\u001b[0m")

class Time:

    @staticmethod
    def doubleDig(digit: int) -> str:
#        print(22 % 10)
        return f"0{digit}" if digit // 10 == 0 else str(digit)

    def __init__(self, hh: int, mm: int, ss: int):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __add__(self, other):
        hh = self.hh + other.hh
        mm = self.mm + other.mm
        ss = self.ss + other.ss

        return Time(hh,mm, ss)

    def __sub__(self, other):

        sss = self.hh * 3600 + self.mm * 60 + self.ss
        sso = other.hh * 3600 + other.mm * 60 + other.ss

        if sss > sso:
            sign = 1
        else:
            sign = -1

        hh = sign * (abs(sss - sso) // 3600)
        mm = sign * (abs(sss - sso) % 60 // 60)
        ss = sign * (abs(sss - sso) % 3600)

        return Time(hh, mm, ss)

    def __mul__(self, other: int):
        if str(other).isdigit():
            hh = self.hh * other
            mm = self.mm * other
            ss = self.ss * other
            return Time(hh,mm, ss)
        else:
            return "Множителем должно быть целое положительное число. Операция не выполнена."


    def __str__(self):

        hh = abs(self.hh)
        mm = abs(self.mm)
        ss = abs(self.ss)
        sign = "-" if self.hh < 0 or self.mm < 0 or self.ss < 0 else ""

        mm = mm + ss // 60
        ss = ss % 60
        hh = hh + mm // 60
        mm = mm % 60

        if hh >= 24:
            dd = hh // 24
            hh = hh % 24
            return f"{sign}{dd} day(s) & {Time.doubleDig(hh)}:{Time.doubleDig(mm)}:{Time.doubleDig(ss)}"
        else:
            return f"{sign}{Time.doubleDig(abs(hh))}:{Time.doubleDig(mm)}:{Time.doubleDig(ss)}"

t1 = Time(27,27,27)
t2 = Time(28,0,1)

print(f"t1:{"\t"*3}", t1)
print(f"t2:{"\t"*3}", t2)
print("t1 + t2:\t", t1 + t2)
print('t2 * "q":\t',t2 * "q")
print('t1 * 4:\t\t',t1 * 4)
print("t1 - t2:\t", t1 - t2)
