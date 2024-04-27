# Eddie Hart
# 10/09/2023
# Word Jumble
# The following program will use a series of while loops and tuppled words and hints that will be scrambled and the
# user has to guess. A hint will also be allowed only on the first round.

import random

print("""            
                    Welcome to Word Jumble!
              Unscramble the letters to make a word
                    Type 'hint' for a hint.
                    """)


words = ("college", "python", "programming", "computer", "keyboard", "word")
hints = ("A place you attend for higher education.",
         "A programming language.",
         "An activity involving the creation of software.",
         "Typically a personal device that allows for browsing media, programming, playing video games, etc.",
         "A device that is used to type into a computer.",
         "A combination of letters and sounds that have a certain meaning attached to it.")

userGuess = ""
playAgain = "y"
score = 0

while playAgain.lower() == "y":
    wordIndex = random.randrange(len(words))
    word = words[wordIndex]
    hint = hints[wordIndex]
    correctWord = word
    jumbledWord = ""
    while word:
        letterPosition = random.randrange(len(word))
        jumbledWord += word[letterPosition]
        word = word[:letterPosition] + word[(letterPosition + 1):]
    print("The jumble is:", jumbledWord)
    userGuess = input("What is the scrambled word? (Type 'hint' for a hint) ")
    if userGuess.lower() == correctWord:
        print("That's it! You guessed it.")
        print("Score: 10")
        score += 10
        print("Overall score:", score)
    elif userGuess.lower() == "hint":
        print(hint)
        while userGuess.lower() != correctWord:
            userGuess = input("Your guess: ")
            if userGuess.lower() == correctWord:
                print("That's it! You guessed it.")
                print("Score: 5")
                score += 5
                print("Overall score:", score)
            else:
                print("Sorry, that's not it.")
    else:
        while userGuess.lower() != correctWord:
            print("Sorry, that's not it.")
            userGuess = input("Your guess: ")
            if userGuess.lower() == correctWord:
                print("That's it! You guessed it.")
                print("Score: 10")
                score += 10
                print("Overall score:", score)
    playAgain = input("Would you like to play again? ")

