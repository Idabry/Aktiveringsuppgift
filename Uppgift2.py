# Write a Python program that:
# 1. Ask the user for their age
# 2. Asks the user if they a driver's license (yes or no)
# 3. Based on the answers, print accordingly:
# "You can drive a car."
# "You are old enough but need a license."
# "You are too young to drive."

age = 18

user_age = int(input("How old are you?: "))
license = input("Do you have a driver's license? (yes or no): ").lower()

if (user_age >= age) and (license == "yes"):
    print("You can drive a car")

elif (user_age >= age) and (license == "no"):
    print("You are old enough, but need a license.")

elif (user_age < age):
    print("You are too young to drive.")
    
else:
    print("Invalid.")