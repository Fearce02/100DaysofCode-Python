#Nested if/else and elif
# if height > 120:
#     print("You can ride the rollerCoaster!")
#     age = int(input("What is your age?"))
#     if age > 18:
#         print("Your ride cost is 12$")
#     elif age >= 12:
#         print("Your ride cost is 7$")    
#     else:
#         print("Your ride cost is 5$")    
# else:
#     print("You cannot ride the rollercoaster :(")
print("Welcome to the RollerCoaster!")

height = int(input("please enter your height in cms"))
bill = 0


#Multiple Ifs

if height >= 120:
    print("you can ride the rollercoaster")

    age = int(input("please enter your age"))

    if age <= 12:
        bill = 5 
        print("Your ticket cost for the ride is 5$")
    elif age <= 18:
        bill = 7
        print("your ticket cost for the ride is 7 $")
    else :
        bill = 12
        print("Your ticket cost for the ride is 12$")

    wants_photo = input("Do you want to take a photo? Press y for Yes and n for No.")

    if wants_photo == "y":
        bill += 3

    print(f"Your Final bill is {bill}")
else : 
    print("Sorry you cannot ride the rollercoaster")
