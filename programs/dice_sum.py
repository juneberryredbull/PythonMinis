import random

rolls = int(input("Enter number of rolls: "))
sum_rolls = 0


while sum_rolls == 0:
    if 1 <= rolls <= 10:
        for i in range(rolls):
            dice_rolls = random.randrange(1, 7)
            sum_rolls += dice_rolls
            print(dice_rolls)
    else:
        rolls = int(input("Try again. Enter number of rolls: "))

print("----------")
print(sum_rolls)
input("")