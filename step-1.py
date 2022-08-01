import os
import random as rnd
from cmath import log

from hangman_art import logo, stages

# Load words file
with open("words.txt", "r", encoding="utf-8") as f:
    word_list = [word.strip() for word in f]

lives = len(stages) - 1

chosen_word = rnd.choice(word_list)
display = ["_" for _ in chosen_word]
end_of_game = False

os.system("clear")
print(chosen_word)
print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(" ".join(display))
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win.")
