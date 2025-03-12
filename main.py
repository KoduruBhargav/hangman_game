import random
from hangman_words import word_list
from hangman_art import *

# printing logo
print(logo)

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

# replace letters with _ (blanks).
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# repeat process until lives gets zero
game_over = False
# create empty list to store guess letters
correct_letters = []

while not game_over:

    print(f"******{lives}/6 LIVES LEFT******")
    guess = input("Guess a letter: ").lower()

    #check if guess is exist: display message
    if guess in correct_letters:
        print('You\'ve already entered')

    # display word status
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            # guess append to list
            correct_letters.append(guess)
        # retrieve previous guess letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # guess not in words reduce lives
    if guess not in chosen_word:
        lives -= 1
        print(f'you choose \'{guess}\', not in chosen word, You lose life')


        if lives == 0:
            game_over = True
            print(f"The correct word is {chosen_word}")

    if "_" not in display:
        game_over = True
        print("******YOU WIN******")

    print(stages[lives])