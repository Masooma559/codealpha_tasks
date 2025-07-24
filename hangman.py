import random

word_list = ['apple', 'bread', 'cloud', 'snake', 'plant']
chosen_word = random.choice(word_list)

guessed_letters = []
tries_left = 6
display = ['_' for _ in chosen_word]

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 chances to guess incorrectly.\n")

while tries_left > 0:
    print("Current word:", ' '.join(display))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.\n")
        continue
    if guess in guessed_letters:
        print("You have already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Good guess!\n")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        tries_left -= 1
        print(f"Wrong guess. You have {tries_left} tries left.\n")

    if '_' not in display:
        print("Congratulations! You guessed the word:", chosen_word)
        print("You win!")
        break

if '_' in display:
    print("You've run out of tries.")
    print("The word was:", chosen_word)
    print("Game over.")
