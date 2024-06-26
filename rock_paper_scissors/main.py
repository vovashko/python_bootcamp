import random

user_choice = input("Let's play RPS. Choose 0 for Rock, 1 for Paper, 2 for Scissors")
if (int(user_choice) == 0):
    print("U chose Rock")
elif (int(user_choice) == 1):
    print("U chose Paper")
elif (int(user_choice) == 2):
    print("U chose Scissors")
AI_choice = random.randint(0,2)
if (int(AI_choice) == 0):
    print("AI chose Rock")
elif (int(AI_choice) == 1):
    print("AI chose Paper")
elif (int(AI_choice) == 2):
    print("AI chose Scissors")
result=[int(user_choice), AI_choice]
if(result == [0, 0] or result == [1,1] or result == [2,2]):
    print("It's a draw!")
elif(result == [0, 1] or result == [1, 2] or result == [2, 0]):
    print("You lost :(")
elif(result == [1, 0] or result == [2, 1] or result == [0, 2]):
    print("You won :)")