import random

initRoll = 6

roll = []
for item in range(initRoll):
    roll.append(random.randint(1,6))

print (roll)

ones = 0

for item in roll:
    if item == 1:
        ones += 1

print (ones)

print ('Test')