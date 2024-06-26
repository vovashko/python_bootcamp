print("HANGMAN")

# Step 1
import random
word_list = ["aardvark", "baboon", "camel"]
lives = 9
chosen_word = random.choice(word_list)
word_guessed = False

display_word = ["_" for letter in chosen_word]
print("".join(display_word))

while (lives > 0 or word_guessed == 1):
    correct_guess = 0
    user_guess = input("\nGuess a letter: ").lower()
    if len(user_guess) > 1:
        print("Please enter only one letter.")
        continue
    letters_guessed = []
    letters_guessed.append(user_guess)
    for letter in chosen_word:
        if letter == user_guess:
            correct_guess = 1
            break 
        else:
            correct_guess = 0

    i = -1
    if correct_guess == 1:
        for letter in chosen_word:
            i += 1
            if letter == user_guess:
                display_word[i] = letter
    elif correct_guess == 0:
        lives -= 1
        print(f"Lives left: {lives}")
    print("".join(display_word))
    print(f"Letters guessed: {", ".join(letters_guessed)}")
    if "_" not in display_word:
        word_guessed = 1
        print("You win!")
        break
    if lives == 0:
        print("You lose!")
        break


