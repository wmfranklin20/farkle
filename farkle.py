import random
import math

from numpy import roll

initRoll = 6

roll = []
for item in range(initRoll):
    roll.append(random.randint(1,6))

print (roll)