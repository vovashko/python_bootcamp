import random

def game (attempts):
    computer_guess = random.randint(1, 100)
    while attempts > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > computer_guess:
            print("Too high.")
        elif user_guess < computer_guess:
            print("Too low.")
        else:
            print("You guessed correctly. Congrats!")
            break
        attempts -= 1
        if (attempts != 0):
            print("Guess again.")
        print(f"You have {attempts} attempts left.")
    if attempts > 0:
        return 0
    else:
        print(f"You lost. Correct guess was {computer_guess}")
        return 1


while True:
    print ("I'm thinking of a number between 1 and 100.")
    difficulty  = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Please type either 'easy' or 'hard' to play.")
        continue
    print(f"You have {attempts} to guess correctly.")
    if game(attempts) == 1:
        print("Want to play again? I'll go easy on you this time.")
        continue_game = input("Type 'yes' or 'no': ")
        if continue_game == "yes":
            continue
        else:
            exit()
    else:
        print("You're good! Wanna play again?")
        continue_game = input("Type 'yes' or 'no': ")
        if continue_game == "yes":
            continue
        else:
            exit()
        
        

