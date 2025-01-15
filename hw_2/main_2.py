#Задача_1

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