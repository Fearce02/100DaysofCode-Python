import random
import hangman_art
from hangman_words import word_list

lives = 6

print(hangman_art.logo)


random_word = random.choice(word_list)


placeholder = ""
word_length = len(random_word)

for position in range(word_length):
    placeholder += "_"
print(f" \n Word to Guess: {placeholder} ")

game_over = False
correct_letters = []

while not game_over:

    print(f" \n ________********You have {lives} left********________ ")
    user_guess = input(" \n guess a letter: ").lower()

    if user_guess in correct_letters:
        print(f"You've already guessed {user_guess}")
    display = ""

    for char in random_word:
        if user_guess == char:
            display += char
            correct_letters.append(user_guess)
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(display)

    if user_guess not in random_word:
        lives -= 1
        print(f" \n You guessed the wrong letter {user_guess}. \nYou lost a life")
        if lives == 0:
            game_over = True
            print(f" \n ____*********You lost*********____ \n The word is {random_word}")

    if "_" not in display:
        game_over = True
        print("____*********You Won!*********____")

    print(hangman_art.stages[lives])