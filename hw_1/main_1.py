# Задача_1

class Animal:

    def __init__(self, name: str, age: int, type: str):
        self.name = name
        self.age = age
        self.type = type

    def makeSound(self):
        print("Звук животного")

    def condition(self):
        print(self.name, self.age, self.type)


# Задача_2

class Book:

    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def openPage(self,n_page: int):
        if n_page <= self.pages:
            print("Страница открылась")
        else:
            print("Страница не открылась")

    def condition(self):
        print(self.name, self.author, self.pages)


# Задача_3

class PassengerPlane:

    def __init__(self, manufacturer: str, model: str, capacity: int, height: int, velocity: int):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.height = height
        self.velocity = velocity

    def takeOff(self):
        print("Самолёт взлетел")

    def landing(self):
        print("Самолёт приземлился")

    def changeHeight(self, new_height: int):
        self.height = new_height

    def changeVelocity(self, new_velocity: int):
        self.velocity = new_velocity


# Задача_4

class MusicAlbum:

    def __init__(self, performer: str, name_album: str, ganre: str, music_list: list):
        self.performer = performer
        self.name_album = name_album
        self.ganre = ganre
        self.music_list = music_list

    def addTrack(self, new_track: str):
        self.music_list.append(new_track)

    def delTrack(self, track_for_delete: str):
        self.music_list.remove(track_for_delete)

    def playTrack(self, track_for_play: str):
        if track_for_play in self.music_list:
            print("Проигрывается трек")
        else:
            print("Трек не найден")


