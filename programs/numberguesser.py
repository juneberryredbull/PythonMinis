# Eddie Hart
# 10/02/2023
# Random Number Game II
# In the following program, the computer will try to guess the user's number.
# The user will be able to tell the computer whether it guessed high or low, or if it correctly guessed the number.

import random

print("     I'll guess the number in 5 guesses!")
print("Think of a number between 1 and 100.")
high = 100
guess = random.randrange(0, 101)
low = 1

for i in range(5, 0, -1):
    print("I have " + str(i) + " guesses remaining")
    userInput = input("Is it " + str(guess) + "? (Yes/High/Low) ")
    if userInput.lower() == "high":
        high = guess
        guess = guess - (high - low) // 2
    elif userInput.lower() == "low":
        low = guess
        guess = guess + (high - low) // 2
    elif userInput.lower() == "yes":
        break
    else:
        while userInput.lower() != "yes" and userInput.lower() != "high" and userInput.lower() != "low":
            userInput = input("Try again. Please answer Yes, High, or Low. ")
        if userInput.lower() == "high":
            high = guess
            guess = guess - (high - low) // 2
        elif userInput.lower() == "low":
            low = guess
            guess = guess + (high - low) // 2
        elif userInput.lower() == "yes":
            break

if i == 1:
    print("I lost!")
    print("The end!")
    input("")
else:
    print("I win!")
    print("The end!")
    input("")












