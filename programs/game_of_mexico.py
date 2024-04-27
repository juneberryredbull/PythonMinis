# Eddie Hart
# 11/13/2023
# Game of Mexico
# The following program will use two user defined functions, one for ascii art and another for the rolls of the dice and their sums
# The main program will play a game of Mexico in which the player with the largest sum wins, with the loser losing a life
# The player who is out of lives loses and the other wins, and the program will ask if the user want to run the simulation again

import random


def mexicoprint():
    print("""

                                          88                         
                                          ""                         
                                                                     
88,dPYba,,adPYba,   ,adPPYba, 8b,     ,d8 88  ,adPPYba,  ,adPPYba,   
88P'   "88"    "8a a8P_____88  `Y8, ,8P'  88 a8"     "" a8"     "8a  
88      88      88 8PP"""""""    )888(    88 8b         8b       d8  
88      88      88 "8b,   ,aa  ,d8" "8b,  88 "8a,   ,aa "8a,   ,a8"  
88      88      88  `"Ybbd8"' 8P'     `Y8 88  `"Ybbd8"'  `"YbbdP"'   

                Welcome to the Game of Mexico!
""")


def rolls_and_sums():
    global p1_sum
    global p2_sum
    global player1_roll
    global player1_roll2
    global player2_roll
    global player2_roll2
    player1_roll = random.randrange(1, 7)
    player1_roll2 = random.randrange(1, 7)
    player2_roll = random.randrange(1, 7)
    player2_roll2 = random.randrange(1, 7)
    p1_sum = player1_roll + player1_roll2
    p2_sum = player2_roll + player2_roll2


answer = "y"
while answer == "y":
    mexicoprint()
    player1_lives = 6
    player2_lives = 6
    while player1_lives != 0 and player2_lives != 0:
        rolls_and_sums()
        print("Player 1 rolled", str(player1_roll), "and", str(player1_roll2), "for a total of", str(player1_roll + player1_roll2))
        print("Player 2 rolled", str(player2_roll), "and", str(player2_roll2), "for a total of", str(player2_roll + player2_roll2))
        if p1_sum > p2_sum:
            player2_lives -= 1
            print("Player 2 loses a life and now has", player2_lives, "lives.")
            print("----------------------------------------------------------")
        elif p1_sum == p2_sum:
            print("It is a tie. No lives lost.")
            print("----------------------------------------------------------")
        else:
            player1_lives -= 1
            print("Player 1 loses a life and now has", player1_lives, "lives.")
            print("----------------------------------------------------------")
    if player1_lives == 0:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
    answer = input("Would you like to run the simulation again? (y/n) ")


