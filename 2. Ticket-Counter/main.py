print("Welcome to Roller Coaster Ticket Counter\n")
amount = 0
height = int(input("What is your height in cm?\n"))

if height >= 150:
    print("You can ride the roller coaster!")

    age = int(input("What is your age?\n"))
    if age < 12:
        amount = 10
    elif age >= 12 and age <= 18:
        amount = 15
    elif age > 18 and age <= 50:
        amount = 20
    else:
        print("You are not eligible to ride the roller coaster.")
else:
    print("Sorry, you have to grow taller before you can ride.")

print(f"Your ticket price is: ${amount}\n")