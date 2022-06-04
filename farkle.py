import random
import math

initRoll = 6

roll = []
for item in range(initRoll):
    roll.append(random.randint(1,6))

print (roll)

class player:
    def __init__(self, name, score, roll):
        self.name = name
        self.score = score
        self.roll = roll

print ('How many players are there?')
numPlayers = int(input())

players = []
for item in range(numPlayers):
    print ("Who is player " + str(item+1) + "?")
    players.append(player(input(), 0, 0))

print('Great! The players are: ')
for item in players:
    print (item.name)