# Eddie Hart
# 10/23/2023
# Email List Part II
# The following program uses a list and a series of if, elif, and while loops to store, preview, and remove emails.
# This is an improved version which will further validate email inputs by checking for @, spaces, ., and domain length
# It will also make it easier for the user to remove emails from the list through numbered emails.

emails = []
choice = None

while choice != "0":
    print("""
            Email List

            0 - Exit
            1 - Show Email List
            2 - Add an Email
            3 - Remove an Email
    """)

    choice = (input("Choice: "))
    if choice == "1":
        if not emails:
            print("The list is empty.")
        else:
            for emailList in emails:
                print(emailList.lower())
    elif choice == "2":
        newEmail = input("Enter an email to add: ")
        atIndex = newEmail.find("@")
        periodIndex = newEmail.find(".")
        if "@" not in newEmail:
            print("The email is missing a '@'. Try again.")
        elif " " in newEmail:
            print("The email cannot contain any spaces. Try again.")
        elif "." not in newEmail:
            print("The email must contain a period (.) Try again.")
        elif atIndex > periodIndex:
            print("The '@' must be followed by a '.' in its domain. Try again.")
        elif len(newEmail) - periodIndex - 1 < 2:
            print("The email must contain a top level domain of at least two characters.")
        else:
            print(newEmail.lower(), "has been added.")
            emails.append(newEmail)
    elif choice == "3":
        if not emails:
            print("The list is empty.")
        else:
            count = 1
            print("Here is the email list.")
            for emailList in emails:
                print(str(count) + ". " + emailList.lower())
                count += 1
            removedEmail = int(input("Which email would you like to remove?: ")) - 1
            if 0 <= removedEmail < len(emails):
                print(emails[removedEmail].lower(), "has been removed.")
                emails.remove(emails[removedEmail])
            else:
                print("Select a valid number.")

    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Sorry, '" + choice + "' isn't a valid choice.")
    input("Press enter key to continue. ")

