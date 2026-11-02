import time

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
        return x / y


while True:

    print("\n==== Calculator ====\n" "1. Add\n" "2. Subtract\n" "3. Multiply\n" "4. Divide\n" "5. Quit")

    time.sleep(0.5)

    navigate = int(input("\nNavigate in the menu, choose between (1-5): "))

    if navigate == 5:
            time.sleep(0.5)
            print("\n")
            print("\t=== Ending program ===\n\n")
            break

    number1 = int(input(f"\nYou choose {navigate}\nEnter a number to use with the operator: "))
    number2 = int(input("Enter a second number: "))

    if navigate == 1:
        print(f"{number1} + {number2} = {add(number1,number2)}")
        time.sleep(0.8)
        

    elif navigate == 2:
        print(f"{number1} - {number2} = {subtract(number1,number2)}")
        time.sleep(0.8)

        
    elif navigate == 3:
        print(f"{number1} * {number2} = {multiply(number1,number2)}")
        time.sleep(0.8)


    elif (number1 == 0) or (number2 == 0):
            print("\nError, can't divide with 0")

            time.sleep(0.8)
              
        
    elif navigate == 4:
        print(f"{number1} / {number2} = {divide(number1,number2)}")
        time.sleep(0.8)
       

    else:
        print("Invalid input, must choose between (1-5)")
        time.sleep(0.8)
        