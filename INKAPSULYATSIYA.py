from uuid import uuid4


class Auto():
    """auto klass"""
    __num_auto = 0

    def __init__(self, make, modul, rangi, yil, narx, km=0):
        """automobilning xususiyati"""
        self.make = make
        self.modul = modul
        self.rangi = rangi
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Auto.__num_auto += 1

    @classmethod
    def get_num_auto(cls):
        return cls.__num_auto

    def get_narx(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km > 0:
            self.__km += km
            return self.__km
        else:
            return "Mashina km kamaytirib bo'lmaydi"
