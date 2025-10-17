import random

def DrawHangman(wrongGuesses):
    print("-------------")
    print("//          \\")
    print("|           |")
    
    # Head
    if wrongGuesses >= 1:
        print("|           O")
    else:
        print("|")
    
    # Body and arms
    if wrongGuesses == 2:
        print("|           |")
    elif wrongGuesses == 3:
        print("|          /|")
    elif wrongGuesses >= 4:
        print("|          /|\\")
    else:
        print("|")
    
    # Legs
    if wrongGuesses == 5:
        print("|          /")
    elif wrongGuesses >= 6:
        print("|          / \\ -You LOSE")
    else:
        print("|")
    
    print("|")
    print("|____________")

def printWord(word, guesses):
    secret = ["_"] * len(word)
    index = 0
    for letter in word:
        if letter in guesses:
            secret[index] = letter
        index += 1
    secret = "".join(secret)
    print(secret)


# Game Logic
word_list = ["python", "hangman", "computer", "science", "sleep", "car", "game"]
word = random.choice(word_list)

guesses = set()
wrongGuesses = 0

print("Welcome to Hangman!")
print(f"The word has {len(word)} letters.")
print("_ " * len(word))
print()

while wrongGuesses <= 6:
    printWord(word, guesses)
    DrawHangman(wrongGuesses)

    # Check for win
    if all(letter in guesses for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guesses:
        print("You have already guessed that letter, please try again.")
        continue

    guesses.add(guess)
    print("Your guesses so far:", guesses)

    if guess not in word:
        wrongGuesses += 1
        print(f"'{guess}' is not in the word.")
    else:
        print(f"Good guess! '{guess}' is in the word.")

    if wrongGuesses >= 6:
        DrawHangman(wrongGuesses)
        print("You lose! The word was:", word)
        break
