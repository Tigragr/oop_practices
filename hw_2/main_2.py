#Задача_1
print()
print("Задача_1_>>>>>>>>>>>")
class Patient:

    def __init__(self, name: str ="Не задано", age: int = 0, disease: str = "Не задано"):
        self.name = name
        self.age = age
        self.disease = disease

    def appointment(self, date: str, time: str):
        self.aboutPatient()
        print("Время записи:", date + " " + time)

    def aboutPatient(self):
        print("Пациент:", self.name, "\n",
              "Возраст:", self.age, "\n",
              "Болезнь:", self.disease)


p = Patient()
p.name = "Вася"
p.age = 18
p.disease = "Энурез"
p.appointment("Дата", "Время")


#Задача_2
print()
print("Задача_2_>>>>>>>>>>>")

class TouristSpot:
    def __init__(self, place: str, land: str, typeShowplace: str):
        self.place = place
        self.land = land
        self.typeShowplace = typeShowplace

    def goPlace(self, nameTourist: str):
        print(f"Tурист {nameTourist} посетил достопримечательность {self.place}, относящуюся к {self.typeShowplace} в стране {self.land}")

    def info(self):
        print(f"Название достопримечательности: {self.place}\nТип достопримечательности: {self.typeShowplace}\nСтрана: {self.land}")


#Задача_3
print()
print("Задача_3_>>>>>>>>>>>")

class ModelWindow:

    topWindow: str
    coordLeftHightPoint: list
    sizeHorizontal: int
    sizeVertical: int
    colorWindow: str
    visibal: bool
    bord: bool

    def __init__(self, topWindow = "ЗАГОЛОВОК", coordLeftHightPoint = [50,50], sizeHorizontal = 100, sizeVertical = 150, colorWindow = "Red", visibal = True, bord = True):
        self.topWindow = topWindow
        self.coordLeftHightPoint = coordLeftHightPoint
        self.sizeHorizontal = sizeHorizontal
        self.sizeVertical = sizeVertical
        self.colorWindow = colorWindow
        self.visibal = visibal
        self.bord = bord

    def moveWindow(self, newCoordLeftHightPoint):
        if newCoordLeftHightPoint[0] >= 1960:
            self.coordLeftHightPoint[0] = 1960
        elif newCoordLeftHightPoint[0] <= 0:
            self.coordLeftHightPoint[0] = 0
        else:
            self.coordLeftHightPoint[0] = newCoordLeftHightPoint[0]

        if newCoordLeftHightPoint[1] >= 1080:
            self.coordLeftHightPoint[1] = 1080
        elif newCoordLeftHightPoint[1] <= 0:
            self.coordLeftHightPoint[1] = 0
        else:
            self.coordLeftHightPoint[0] = newCoordLeftHightPoint[0]

    def resizeWindow(self, changeSizeHorizontal, changeSizeVertical):
        if self.coordLeftHightPoint[0] + changeSizeHorizontal >= 1960:
            self.sizeHorizontal = 1960 - self.coordLeftHightPoint[0]
        if changeSizeHorizontal <= 0:
            self.sizeHorizontal = 1
        else:
            self.sizeHorizontal += changeSizeHorizontal


        if self.coordLeftHightPoint[1] + changeSizeVertical >= 1080:
            self.sizeVertical = 1080 - self.coordLeftHightPoint[1]
        if changeSizeVertical <= 0:
            self.sizeVertical = 1
        else:
            self.sizeVertical += changeSizeVertical

    def changeColor(self, newColor):
        self.color = newColor

    def vision(self, newVisibal):
        self.visibal = newVisibal
        vis = "Окно видимо" if self.visibal else "Окно не видимо"
        print(vis)

    def __str__(self):
        str_topWindow = str(self.topWindow)
        str_coordLeftHightPoint = f"[{self.coordLeftHightPoint[0]}, {self.coordLeftHightPoint[1]}]"
        str_sizeHorizontal = str(self.sizeHorizontal)
        str_sizeVertical = str(self.sizeVertical)
        str_colorWindow = str(self.colorWindow)
        str_visibal = str(self.visibal)
        str_bord = str(self.bord)
        print(f"Заголовок окна: {str_topWindow},\n"
              f"Координаты верхнего левого угла окна: {str_coordLeftHightPoint},\n"
              f"Ширина окна: {str_sizeHorizontal},\nВысота окна: {str_sizeVertical},\n"
              f"Цвет окна: {str_colorWindow},\nВидимость окна: {str_visibal},\nВидимость границ: {str_bord}")

ModelWindow().__str__()


#Задача_4
print()
print("Задача_4_>>>>>>>>>>>")

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
    def inversList(lst: list) -> list:

        res = []
        for el in lst:
            res.insert(0,el)

        return res

    @staticmethod
    def maxElement(lst: list) -> int:

        maxEl = lst[0]
        for el in lst:
            if el > maxEl:
                maxEl = el

        return maxEl

    @staticmethod
    def minElement(lst: list) -> int:

        minEl = lst[0]
        for el in lst:
            if el < minEl:
                minEl = el

        return minEl


#Задача_5
print()
print("Задача_5_>>>>>>>>>>>")

# Разработайте класс Vector для представления и манипуляции векторами в трехмерном пространстве.

# Включите методы для сложения, вычитания, скалярного произведения и векторного произведения векторов.
# Перегрузите операторы (+, -, *) для соответствующих операций: + для сложения векторов, - для вычитания,
# * может использоваться как для скалярного произведения, так и для векторного в зависимости от типа аргумента (вектор или число).
# Реализуйте также метод для вычисления нормы (длины) вектора.


class Vector:

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z

        return new_x, new_y, new_z

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z

        return new_x, new_y, new_z

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        new_z = self.z * other.z

        return new_x, new_y, new_z
########################################################################################

    def __str__(self):
        return f'Координаты вектора: "{self.x,self.y,self.z}"'

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)

vv = v1 + v2
print(vv)




