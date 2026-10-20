
import random

# Hangman Game - ShadowFox Task 2

words = ["python", "computer", "program", "science", "developer"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("=" * 35)
print("       WELCOME TO HANGMAN")
print("=" * 35)
print("Guess the hidden word, one letter at a time!")
print("You have", attempts, "wrong guesses available.")
print()

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Attempts remaining:", attempts)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        print("YOU WIN!")
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        print()
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        print()
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

    print()

else:
    print("Word:", " ".join(word))
    print("Game over! The correct word was:", word)

print("\nThank you for playing Hangman!")
