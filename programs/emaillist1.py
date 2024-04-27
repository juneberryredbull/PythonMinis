# Eddie Hart
# 10/16/2023
# Email List Part I
# The following program uses a list and a series of if, elif, and while loops to store, preview, and remove emails

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
                print(emailList)
    elif choice == "2":
        newEmail = input("Enter an email to add: ")
        if "@" in newEmail:
            print(newEmail, "was added.")
            emails.append(newEmail)
        else:
            print("The email must contain an '@' symbol.")
    elif choice == "3":
        if not emails:
            print("The list is empty.")
        else:
            print("Here is the email list.")
            for emailList in emails:
                print(emailList)
            removedEmail = input("Type the email to remove: ")
            if removedEmail in emails:
                emails.remove(removedEmail)
                print(removedEmail, "has been removed.")
            else:
                print("That email isn't on the list.")
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Sorry, '" + choice + "' isn't a valid choice.")
    input("Press enter key to continue.")
