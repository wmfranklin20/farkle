import random

initRoll = 6

roll = []
for item in range(initRoll):
    roll.append(random.randint(1,6))

print (roll)