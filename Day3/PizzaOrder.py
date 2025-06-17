print("Welcome to the Pizza Shop!")

size = input("What size pizza do you want? type S for small, M for Medium, L for Large :")
pepperoni = input("DO you want Pepperoni? type Y for yes and N for no :")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N :")
bill = 0

if size == "S" :
    bill += 15
    print("Small size selected")
elif size == "M" :
    bill +=20
    print("medium size selected")
elif size == "L" :
    bill +=25
    print("Large size selected")

if pepperoni == "Y":
    if size == "S":
        bill +=2
    else :
        bill += 3

    print("Pepperoni Added!")

if extra_cheese == "Y" :
    bill += 1
    print("extra Cheese Added!")

print(f"Your final bill is {bill}")





