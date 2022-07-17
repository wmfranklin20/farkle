# farkle.py
Basic Farkle program in Python

Currently the file is seperated into three sub-files, one focused on setting up player order and classes,  a second to build the program for deciding rolls and how many dice are kept and a third to house the scoring rules. These files are then merged in a main farkle.py file.

## Player Setup:

Takes player names as user input, and randomly selects a starting player from the input list.  Note, order will follow however the user types the the names of players as they are ordered around the table, the program will pick a random start point but maintain the order of the table.


## Scoring Mechanisms:

Starting with an initial dice roll of 6 die, for example:

[5,3,4,3,2,1]

This set is cast to a new list totaling the number of each die:

[1,1,2,1,1,0]

Then, this set is tested against the scoring library to score the current roll:

[100,0,0,0,50,0] = 150
