f# Eddie Hart
# 9/25/2023
# Random Number Game
# The following program pseudo-randomly generates a number between 1-100 that the player has to guess.
# The player has 5 chances to guess the number. At the end of each game, the player is given a choice to either keep playing or quit.

import random

print("     I'll guess the number in 5 guesses!")
print("Think of a number between 1 and 100")
answer = "y"

while answer == "y" or answer == "Y":
    number = random.randrange(1, 101)
    for i in range(4, -1, -1):
        guess = int(input("Guess the number: "))
        if guess > number:
            print("Too high!")
            print(i, "guesses remaining.")
        elif guess < number:
            print("Too low!")
            print(i, "guesses remaining.")
        else:
            break
    if i == 0:
        print("The number was " + str(number) + ".")
    else:
        print("You win!")
    answer = input("Would you like to play again? ")











