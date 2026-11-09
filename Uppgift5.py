
#                  Moment 5: inlämningsuppgift
import time

contacts = []

while True:
    print("\n===== CONTACT LIST ======\n",
          "1. Add a contact\n", 
          "2. Show all contacts\n", 
          "3. Search for a contact\n",
          "4. Remove a contact\n",
          "5. Quit\n")

    user_input = int(input("\nCheck the menu and pick one to navigate to: "))

    if user_input == 5:
        print("\nEnding program..")
        break

    elif user_input == 1:
        name = input("\nAdd a name to the list: ").lower()
        contacts.append(name)
        time.sleep(0.5)

    elif user_input == 2:
        print(contacts)
        time.sleep(1.5)

    elif user_input == 3:
        name_checker = input("\nEnter a name to check if its in the list: ").lower()
        if name_checker in contacts:
            time.sleep(1.5)
            print(f"The name you entered exists in the list :D")
            time.sleep(1.5)

        else:
            print("\nThe name you entered does not exist in the list :(")
            time.sleep(1.5)

    elif user_input == 4:
        remove_name = input("\nWrite a name in the list to remove: ").lower()
        if remove_name in contacts:
            contacts.remove(remove_name)
            time.sleep(1.5)

    else:
        print("\nInvalid input, choose between 1-5")
        time.sleep(1.5)
