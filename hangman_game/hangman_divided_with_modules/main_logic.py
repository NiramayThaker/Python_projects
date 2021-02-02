import random
from hangman_game.hangman_divided_with_modules import list_of_words
import ui_ux

# word_list = ["king", "shiva", "niramay", "pythonista"]
chosen_word = random.choice(list_of_words.word_list)

print(chosen_word)

word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += '_'

lives = 6
end_of_game = False

print(ui_ux.logo)
print("\nYOU WILL HAVE -- 6 -- LIVES")
while not end_of_game:
    guessed_letter = input("Guess any letter -> ").lower()

    if guessed_letter in chosen_word:
        print(f"The letter you guessed is in the list")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = letter

    if guessed_letter not in chosen_word:
        lives = lives - 1
        print(f"\nYou loss lives, lives = {lives}")
        print(ui_ux.hangman_stages[lives])

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won")
        print(f"lives left = {lives}")
    elif lives == 0:
        print("You loss")
        break
