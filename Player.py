class Player:
    def __init__(self, initName):
        self.__hand = []
        self.__name = initName

    def get__name(self):
        return self.__name

    def get__hand(self):
        return self.__hand

    def getHandSize(self):
        return len(self.__hand)

    def addCard(self, card):
        self.__hand += card

    def removeCard(self, card):
        for i in self.__hand:
            if i == card:
                self.__hand.remove(i)

    def sort(self, card, isAI):
        playable = []
        un_playable = []
        x = 0
        for i in self.__hand:
            if self.__hand[x][0] == card[0] or self.__hand[x][1] == card[1]:
                playable.append(i)
            elif card[1] == 'W' and self.__hand[x][0] == card[0]:
                playable.append(i)
            elif card[1] == 'F' and self.__hand[x][0] == card[0]:
                playable.append(i)
            elif self.__hand[x] == "XF" or self.__hand[x] == "XW":
                playable.append(i)
            else:
                un_playable.append(i)
            x += 1

        if not isAI:
            print(str(playable) + "\n")
            print(str(un_playable) + "\n")
        return playable

    def play(self, card, isAI):
        # STILL NEEDS CODE FOR USER TO DRAW FROM THE DECK THIS MAY NEED SOME DISCUSSING SINCE PLAYER DOESNT HAVE ACCESS TO THE DECK
        # I WAS THINKING WE JUST RETURN "DECK" AS THE CARD AND THEN IN GAME WE CHECK IF "DECK" WAS THE RETURNED CARD AND DEAL WITH IT THERE
        # I can work on it just give me a sec... a couple minutes
        played_card = ""
        if isAI:
            return self.AI_play(card)
        playable_cards = self.sort(card, isAI)
        played_card = input("Enter the card you'd like to play or enter D to draw from the deck: ")
        playable_cards.append("D")
        while played_card not in playable_cards:
            played_card = input("Card is not playable. Please select another card")

        self.removeCard(played_card)

        if played_card[0] == "X":
            c = input("What would you like the color to change to? ")
            if played_card[1] == "F":
                played_card = c + "F"
            else:
                played_card = c + "W"

        return played_card

    def AI_play(self, card):
        t = self.sort(card, True)
        t.append("D")
        st = t[0]
        if t[0] != "D":
            self.removeCard(t[0])

        if st[0] == "X":
            tracker = {'R': 0, 'Y': 0, 'G': 0, 'B': 0}
            for i in self.get__hand():
                if i[0] == "R":
                    tracker['R'] += 1
                elif i[0] == "Y":
                    tracker["Y"] += 1
                elif i[0] == "G":
                    tracker["G"] += 1
                elif i[0] == "B":
                    tracker["B"] += 1
            v = list(tracker.values())
            k = list(tracker.keys())
            a = k[v.index(max(v))]

            t[0] = a + st[1]

        return t[0]