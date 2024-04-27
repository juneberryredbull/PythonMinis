# Eddie Hart
# 10/7/2023
# Backwards string
# The following program will use a for loop, string indexing, and concatenation to reverse the user's input

userString = input("Enter a string: ")
backwardString = ""

for i in range(len(userString)-1, -1, -1):
    backwardString += userString[i]

print(backwardString)