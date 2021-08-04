from Deck import Deck
from Game import Game

USERNAME = ""
ORDER = []


print("Welcome to UNO!\n\nEnter your name: ")
USERNAME = input()

g = Game(USERNAME)

have_winner = False

print(USERNAME + ", The game is starting!\n\n")

while not have_winner:
    have_winner = g.next_play()