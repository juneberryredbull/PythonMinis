# Eddie Hart
# 10/02/2023
# Dice Roll II Assignment
# The following program will simulate a user dice roll and a computer dice roll.
# The computer will try to match the user's dice roll, and print how many rolls it took to match it.

import random

userRoll = random.randrange(1,7)
computerRoll = random.randrange(1,7)
rollCounter = 1

print("I rolled", userRoll)
print("Computer rolled", computerRoll)
while computerRoll != userRoll:
    computerRoll = random.randrange(1,7)
    print("Computer rolled", computerRoll)
    rollCounter += 1

print("It took the computer " + str(rollCounter) + " rolls to match mine")
input("Press enter to continue...")



