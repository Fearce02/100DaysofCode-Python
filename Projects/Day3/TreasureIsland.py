print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

sides = input("Please choose left or right. Enter 'left' to go Left and 'right' to go Right")

if sides == "right":
    print("You fell into a hole. Game Over!")

elif sides == "left":
    print("You have arrived at a Lake!")
    boat = input("Do you want to swim or wait for a boat?")
    if boat == "swim":
        print("You were attacked by a trout. Game Over!")
    elif boat == "wait":
        print("You have Arrived at a Room with 3 doors. Choose the right door to find the treasure!")
        door = input("Please Choose a Door. 'Red', 'Yellow' or 'Blue'")
        if door == 'Red':
            print("Burned by fire! Game Over.")
        elif door == 'Blue':
            print("Eaten by a beast. Game Over!")
        elif door == 'Yellow':
            print("You have found the treasure!. You won!")