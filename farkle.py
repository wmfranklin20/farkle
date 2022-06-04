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

a = input()

print (type(a))