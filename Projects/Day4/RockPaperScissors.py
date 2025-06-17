import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

items_list = [rock, paper, scissors]
computer_input = random.choice(items_list)
user_input = int(input("What Do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if user_input >= 0 and user_input <= 2:
    user_print = items_list[user_input]

if user_input == 0 and computer_input == rock:
    print(user_print)
    print(computer_input)
    print("The game is tied")

elif user_input == 1 and computer_input == rock:
    print(user_print)
    print(computer_input)
    print("You won!")

elif user_input == 2 and computer_input == rock:
    print(user_print)
    print(computer_input)
    print("You Lost")

elif user_input == 0 and computer_input == paper:
    print(user_print)
    print(computer_input)
    print("You Lost")

elif user_input == 1 and computer_input == paper:
    print(user_print)
    print(computer_input)
    print("Game Tied")

elif user_input == 2 and computer_input == paper:
    print(user_print)
    print(computer_input)
    print("You Won!")

elif user_input == 0 and computer_input == scissors:
    print(user_print)
    print(computer_input)
    print("You Won!")

elif user_input == 1 and computer_input == scissors:
    print(user_print)
    print(computer_input)
    print("You Lost!")

elif user_input == 2 and computer_input == scissors:
    print(user_print)
    print(computer_input)
    print("Game Tied")

else:
    print("You typed an invalid number")    


