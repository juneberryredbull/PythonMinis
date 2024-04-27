# Eddie Hart
# 10/30/2023
# Find the Largest
# The following program uses a list and a series of if, elif, and while loops to store, preview, and remove emails.

numbers = []
nums = 0

def find_the_largest(nums):
    while nums != -1:
        for i in range(5):
            nums = int(input("Enter a number between 1 and 100. (-1 to stop):"))
            if -1 > nums > 100:
                nums = int(input("Try again! Enter a number between 1 and 100:"))
            numbers.append(nums)
        print("The numbers are", numbers)
        print("The largest number is")
        break

find_the_largest(nums)