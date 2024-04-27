# Eddie Hart
# Tip Calculator Assignment
# 9/4/2023

# The following commands will run a series of input, float, print, and arithmetic commands in order to create a tip calculator

svname = input("Input Server's Name: ")
check_amount = float(input("Input Check Amount: $"))
tip_percent = int(input("Enter Tip % in Whole Numbers: %"))
tip_amount = tip_percent/100 * check_amount
total = tip_amount + check_amount




print("""





Receipt""")
print("-----------------------")
print("Server Name:", svname)
print("Check Amount: $ %.2f" % check_amount)
print("Tip Amount: $ %.2f" % tip_amount)
print("Total Amount: $ %.2f" % total)
input("")
