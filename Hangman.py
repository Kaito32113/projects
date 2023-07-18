import random

def hangman():
    words = ["orange", "banana", "cherry", "chocolate", "elderberry", "fudge", "grape", "frog", "goat", "Sanskriti",]
    word = random.choice(words)
    guessed_letters = []
    tries = 10

    while tries > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        if guessed_word == word:
            print(f"Congratulations! You guessed the word: {word}")
            break

        print(f"Word: {guessed_word}")
        print(f"Tries left: {tries}")

        guess = input("Guess a letter: ")
        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Wrong guess!")

    if tries == 0:
        print(f"Sorry, you lost. The word was: {word}")

hangman()
