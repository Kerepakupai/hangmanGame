import random
import os
from hangman_art import logo, stages


def load_words(file):
    words = []
    with open(file, 'r', encoding='UTF-8') as f:
        for word in f:
            words.append(word)

    return words


def main():
    word_list = load_words('words.txt')
    chosen_word = random.choice(word_list)

    end_of_game = False
    lives = len(stages) - 1
    display = ['_' for i in range(len(chosen_word) - 1)]

    while not end_of_game:
        print(logo)
        print(' '.join(display))
        print(stages[lives])
        guess = input('\nGuess a letter: ').lower()

        os.system('cls')

        if guess in display:
            print(f'You\'ve already guessed {guess.upper()}!')
        else:
            for i, letter in enumerate(chosen_word):
                if guess == letter:
                    display[i] = letter

            if guess not in chosen_word:
                print(f'You guessed {guess.upper()}, that\'s not in the word. You lose a life.')
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print(stages[lives])
                    print(f'The word to guessed was {chosen_word.upper()}')
                    print('You lose!')

            if '_' not in display:
                end_of_game = True
                print('You win!')


if __name__ == '__main__':
    main()
