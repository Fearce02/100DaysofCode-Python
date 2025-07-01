import random

logo = print("""                                                             
 _____           _              _____                         
|   | |_ _ _____| |_ ___ ___   |   __|_ _ ___ ___ ___ ___ ___ 
| | | | | |     | . | -_|  _|  |  |  | | | -_|_ -|_ -| -_|  _|
|_|___|___|_|_|_|___|___|_|    |_____|___|___|___|___|___|_|  
                                                              """)

print("Welcome to the Number Guessing Game!")

random_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty level: Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    no_of_attempts = 10
elif difficulty == "hard":
    no_of_attempts = 5
else:
    print("Invalid difficulty level. Please restart the game and choose 'easy' or 'hard'.")

while no_of_attempts > 0:
    print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue
    if guess == random_number:
        print(f"You got it! The number was {random_number}.")
        break
    elif guess < random_number:
        print("Too low.")
    else:
        print("Too high.")
    no_of_attempts -= 1
if no_of_attempts == 0:
    print(f"You've run out of attempts. The number was {random_number}. Better luck next time!")

