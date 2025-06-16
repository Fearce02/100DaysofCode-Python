#Nested if/else and elif

print("Welcome to the RollerCoaster!")

height = int(input("please enter your height in cms"))

if height > 120:
    print("You can ride the rollerCoaster!")
    age = int(input("What is your age?"))
    if age > 18:
        print("Your ride cost is 12$")
    elif age >= 12:
        print("Your ride cost is 7$")    
    else:
        print("Your ride cost is 5$")    
else:
    print("You cannot ride the rollercoaster :(")