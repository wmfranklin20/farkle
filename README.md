# farkle.py
Basic Farkle program in Python

Currently the file is seperated into two files, one focused on setting up player order and classes, and a second to build the program for deciding rolls and how many dice are kept.


## Scoring Mechanisms:

Starting with an initial dice roll of 6 die, for example:

[5,3,4,3,2,1]

This set is cast to a new list totaling the number of each die:

[1,1,2,1,1,0]

Then, this set is tested against the scoring library to score the current roll:

[100,0,0,0,50,0] = 150