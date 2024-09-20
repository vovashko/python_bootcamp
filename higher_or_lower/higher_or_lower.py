import random
import game_data

person_a = {}
person_a = game_data.data[random.randint(0, len(game_data.data) - 1)]

person_b = {}
person_b = game_data.data[random.randint(0, len(game_data.data) - 1)]

score = 0
# welcome message first person

while True:
    print(f"Compare A: {person_a["name"]}, {person_a["description"]} from {person_a["country"]}")
    print(f"Against B: {person_b["name"]}, {person_b["description"]} from {person_b["country"]}")
    response = input("Who has more followers? Type 'A' or 'B': ")
    if (response == "A"):
        if person_a["follower_count"] >= person_b["follower_count"]:
            person_a = person_b
            person_b = game_data.data[random.randint(0, len(game_data.data) - 1)]
            score += 1
            print(f"You are right. Current score: {score}")
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            break
    elif(response == "B"):
        if person_b["follower_count"] >= person_a["follower_count"]:
            person_a = person_b
            person_b = game_data.data[random.randint(0, len(game_data.data) - 1)]
            score += 1
            print(f"You are right. Current score: {score}")
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            break

