import time

while True:
    print("\n\n==== MENU ==== \n1. Say hello \n2. Show numbers 1–5 \n3. Multiply two numbers \n4. Quit")
    time.sleep(0.6)
    user_input = int(input("\nNavigate in the menu (Write one of the numbers): "))

    if user_input == 1:
        time.sleep(1)
        print("\nHello!\n\n")
        time.sleep(1)

    elif user_input == 2:
        for numbers in range(1,6):
            print(numbers)
            time.sleep(0.4)
        time.sleep(1)

    elif user_input == 3:
        number1 = int(input("\nPick any number: "))
        time.sleep(0.6)
        number2 = int(input("Pick a second number: "))
        total = number1 * number2
        time.sleep(1)
        print(f"{number1} * {number2} = {total}\n\n")
        time.sleep(1)

    else:
        time.sleep(1)
        print("\nQuitting program")
        break