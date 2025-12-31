print("Welcome to Pizza Deliveries!\n")

size = input("What size pizza do you want? S, M, or L\n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N\n").lower()
extra_cheese = input("Do you want extra cheese? Y or N\n").lower()

price = 0

if size == "s":
    price += 15
elif size == "m":
    price += 20
elif size == "l":
    price += 25
else:
    print("Invalid selection.")
    exit()    


if add_pepperoni == "y":
    if size == "s":
        price += 2
    else:
        price += 3    
  

if extra_cheese == "y":
    price += 1
else:
    price += 0             

print(f"Your final bill is: ${price}\n")    