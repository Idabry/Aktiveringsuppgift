import time

## Första koden nedan är markerad som "kommentar" men vill ha med den för att visa vad som gjordes innan

# with open("todolist.txt", "w") as file:           - Detta skapar en ny fil som heter "todolist.txt"
#    pass

# with open("todolist.txt", "w")as file:
#    file.write("TASKS:\n\n")          - Detta skriver först TASKS: i filen

# tasks = ["clean apartment", "wash clothes", "study"]   - Detta skapar en variabel med listan av allt jag vill ha i filen

# with open("todolist.txt", "a") as file:
#    for task in tasks:
#        file.write(task + "\n")       - Detta lägger till allt i filen med ett radhopp mellan varje sak i listan


while True:
    print("\n=== TO-DO LIST ===\n", "1. View tasks\n", "2. Add task\n", "3. Remove task\n", "4. Quit")
    navigate = int(input("\nChoose one of the options 1-4: "))
    print("\n")
    time.sleep(0.5)

    if navigate == 1:
        with open("todolist.txt", "r") as file:
            content = file.read()
            print(content)
        time.sleep(1)

    elif navigate == 2:
        add = input("What do you wish to add to the list?: ").lower()
        with open("todolist.txt", "a") as file:
            file.write(add +"\n")
        time.sleep(1)

    elif navigate == 3:
        remove = input("What do you wish to remove from the list?: ").lower()
        with open("todolist.txt", "r") as file:
            tasks = file.readlines()
        print(f"Removing: {remove}...")

        updated_tasks = []
        for task in tasks:
            if task.strip() != remove:
                updated_tasks.append(task)
        with open("todolist.txt", "w") as file:
            file.writelines(updated_tasks)
        time.sleep(1)

    elif navigate == 4:
        print("Ending program..")
        print("\n")
        break

    else:
        print("Invalid input, must choose an option between 1-4")
        time.sleep(1)