from Card import Card

from random import randrange

class Deck:
    def __init__(self):
        self.__deckList = []
        self.createSpecials()
        self.createColor("R")
        self.createColor("B")
        self.createColor("G")
        self.createColor("Y")
        self.shuffle()

    def get__deckList(self):
        return self.__deckList

    def createSpecials(self):
        for x in range (0, 4):
            self.__deckList.append("XW")
            self.__deckList.append("XF")

    def createColor(self, color):
        self.__deckList.append(color + "0")

        self.__deckList.append(color + "S")
        self.__deckList.append(color + "S")

        self.__deckList.append(color + "R")
        self.__deckList.append(color + "R")

        self.__deckList.append(color + "T")
        self.__deckList.append(color + "T")

        for x in range (1, 10):
            self.__deckList.append(color + str(x))
            self.__deckList.append(color + str(x))

    def checkSize(self, num):
        if len(self.__deckList) >= num:
            return True
        return False

    def shuffle(self):
        for x in range(0, 3):
            temp = self.__deckList
            self.__deckList = []
            for x in range(0, len(temp)):
                i = randrange(len(temp))
                self.__deckList.append(temp.pop(i))

    def draw(self, num):
        cards = []
        for x in range(0, num):
            cards.append(self.__deckList.pop(0))
        return cards

    def resetDeck(self, board):
        self.__deckList = board[0 : len(board) - 1]
        del board[0 : len(board) - 1]
        shuffle()

    def __str__(self):
        out = ""
        for card in self.__deckList:
            out += card
            out += " "
        return out