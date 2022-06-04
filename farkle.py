import random
import math

#initialize player list
class player:
    def __init__(self, name, order, score, roll):
        self.name = name
        self.score = score
        self.roll = roll

#hardcoded player list for testing
numPlayers = 3
players = [player('Will', 0,0,0),player('Emily',0,0,0), player('Calvin',0,0,0)]

#print ('How many players are there?')
#numPlayers = int(input())

#players = []
#for item in range(numPlayers):
    #print ("Who is player " + str(item+1) + "?")
    #players.append(player(input(), 0, 0, 0))

print('Great! The players are: ')
for item in players:
    print (item.name)


first = random.randint(0,(len(players)-1))
print (first)
print (players[first].name + " is first!")

a = []
for item in players:
    if first <= (len(players)-1):
        a.append(first)
        first = first + 1
    elif first == (len(players)):
        first = 0
        a.append(first)
        first = first + 1

print (a)





initRoll = 6

roll = []
for item in range(initRoll):
    roll.append(random.randint(1,6))

print (roll)