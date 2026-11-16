current_year = 2026

first_name = input("\nWhat is your first name?: ")
last_name = input("What is your last name?: ")
birth_year = int(input("What year were you born?: "))
height = float(input("How tall are you? (Write in centimeters): "))
country = input("What country do you live in?: ")
hobby = input("What is your favorite hobby?: ")

age = current_year - (birth_year)
height_in_meter = (height / 100)


print("\n===== Personal Information Summary =====")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Height: {height_in_meter} meters")
print(f"Country: {country}")
print(f"Hobby: {hobby}")
print("==========================================")