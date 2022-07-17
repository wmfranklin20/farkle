import random

#initial roll of six dice
initRoll = 6

roll = []
for item in range(initRoll):
    roll.append(random.randint(1,6))

print ("Player rolled: " + str(roll))

uniqueDie = []
for item in roll:
    if item not in uniqueDie:
        uniqueDie.append(item)
#print(uniqueDie)

#define counter list for number of each dice rolled
rollScore = [0,0,0,0,0,0]

for item in roll:
    if item == 1:
        rollScore[0] += 1
    elif item == 2:
        rollScore[1] += 1
    elif item == 3:
        rollScore[2] += 1
    elif item == 4:
        rollScore[3] += 1
    elif item == 5:
        rollScore[4] += 1
    elif item == 6:
        rollScore[5] += 1       

print ("Number of each dice rolled: " + str(rollScore))

uniqueScore = []
for item in rollScore:
    if item not in uniqueScore:
        uniqueScore.append(item)
print(uniqueScore)

#scoring based on current dice roll
score = 0

for idx, item in enumerate(rollScore):
    print (item)
    if item == 3:
        score = ((int(idx)+1) * 100)
    elif item == 4:
        score = 1000

print (score)