class Card():
    def __init__(self, initValue, initColor):
        self.__value = initValue
        self.__color = initColor

    def set__color(self, initColor):
        self.__color = initColor

    def set__value(self, initValue):
        self.__value = initValue

    def get__color(self):
        return self.__color

    def get__value(self):
        return self.__value