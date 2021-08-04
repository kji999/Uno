from Card import Card
from Deck import Deck
from Player import Player
from random import randrange


class Game:

    def __init__(self, username):
        self.deck = Deck()

        self.player0 = Player("Rabbit")
        self.player1 = Player("Horse")
        self.player2 = Player("Thumb in the bootyhole PLZ")
        self.player3 = Player(username)

        self.board = []
        self.order = []
        self.turn = 0
        self.direction = 1  # 1 up, -1 down
        self.distributeCards()
        self.randomizeOrder()
        self.initBoard()

    def next_play(self):
        played_card = ""
        if self.order[self.turn] == self.player0:
            print("{}'s hand: {} ".format(self.player0.get__name(), self.player0.get__hand()))
            played_card = self.player0.play(self.board[-1], True)
            print(self.player0.get__name() + " played " + played_card)
            self.cardD(self.turn, played_card, self.player0)

        elif self.order[self.turn] == self.player1:
            print("{}'s hand: {} ".format(self.player1.get__name(), self.player1.get__hand()))
            played_card = self.player1.play(self.board[-1], True)
            print(self.player1.get__name() + " played " + played_card)
            self.cardD(self.turn, played_card, self.player1)

        elif self.order[self.turn] == self.player2:
            print("{}'s hand: {} ".format(self.player2.get__name(), self.player2.get__hand()))
            played_card = self.player2.play(self.board[-1], True)
            print(self.player2.get__name() + " played " + played_card)
            self.cardD(self.turn, played_card, self.player2)

        else:
            self.displayBoard()
            played_card = self.player3.play(self.board[-1], False)
            self.cardD(self.turn, played_card, self.player3)

        return False

    def cardD(self, player, played_card, p):
        if played_card == "D":
            self.draw(player, 1)
            self.update_turn()
        else:
            self.process_play(played_card)

    def determine_next_player(self):
        if self.direction == -1 and self.turn == 0:
            return len(self.order) - 1
        elif self.direction == 1 and self.turn == len(self.order) - 1:
            return 0
        return self.turn + self.direction

    def update_turn(self):
        print("Current: {}, Next: {}".format(self.order[self.turn].get__name(),
                                             self.order[self.determine_next_player()].get__name()))

        if self.order[self.turn].getHandSize() == 0:
            print("{} is OUT!".format(self.order[self.turn].get__name()))
            print("{} has been removed from the order".format(self.order[self.turn].get__name()))
            self.order.remove(self.order[self.turn])
            self.turn -= 1

        self.turn = self.determine_next_player()

    def getUserHand(self):
        hand = ""
        usrHand = self.player3.get__hand()
        for card in usrHand:
            hand += card
            hand += " "
        return hand

    def distributeCards(self):
        for x in range(0, 7):
            self.player0.addCard(self.deck.draw(1))
            self.player1.addCard(self.deck.draw(1))
            self.player2.addCard(self.deck.draw(1))
            self.player3.addCard(self.deck.draw(1))

    def initBoard(self):
        temp = self.deck.get__deckList()[0][1]
        while not temp.isnumeric():
            self.deck.shuffle()
            l = self.deck.get__deckList()
            temp = self.deck.get__deckList()[0][1]
        self.board.append(self.deck.draw(1)[0])
        self.displayBoard()
        print("\n\n{}'s hand: {}".format(self.player0.get__name(), self.player0.get__hand()))
        print("{}'s hand: {}".format(self.player1.get__name(), self.player1.get__hand()))
        print("{}'s hand: {}\n\n".format(self.player2.get__name(), self.player2.get__hand()))

    def randomizeOrder(self):
        temp = [self.player0, self.player1, self.player2, self.player3]

        for x in range(0, len(temp)):
            i = randrange(len(temp))
            self.order.append(temp.pop(i))
        n = 0
        print("Initial Order: ")
        for i in self.order:
            print(self.order[n].get__name())
            n += 1

    def displayBoard(self):
        print("\n{}: {} cards".format(self.player0.get__name(), self.player0.getHandSize()))
        print("{}: {} cards".format(self.player1.get__name(), self.player1.getHandSize()))
        print("{}: {} cards".format(self.player2.get__name(), self.player2.getHandSize()))
        print("\nBoard: {}".format(self.board[-1]))

    def process_play(self, card):
        if card[1] == 'S':
            self.update_turn()
        elif card[1] == 'R':
            self.direction *= -1
        elif card[1] == 'T':
            self.draw(self.determine_next_player(), 2)
            self.update_turn()
        elif card[1] == 'F':
            self.draw(self.determine_next_player(), 4)
            self.update_turn()

        if self.board[-1][1] == 'W':
            self.board[-1] = "XW"
        if self.board[-1][1] == 'F':
            self.board[-1] == "XF"

        self.board.append(card)
        self.update_turn()

    def draw(self, player, num_cards):
        # check size of deck first before processing this, empty deck before calling reset deck
        if self.order[player] == self.player0:
            self.player0.addCard(self.deck.draw(num_cards))
        elif self.order[player] == self.player1:
            self.player1.addCard(self.deck.draw(num_cards))
        elif self.order[player] == self.player2:
            self.player2.addCard(self.deck.draw(num_cards))
        else:
            self.player3.addCard(self.deck.draw(num_cards))

    def restartGame(self):
        pass