import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 10, 10, 10]

def check_score(hand):
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


while True:
    response = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")
    if response == "no":
        break
    elif response != "yes":
        print("Invalid response. Please type 'yes' or 'no'.")
        continue
    else:
        your_hand = [random.choice(cards), random.choice(cards)]
        dealer_hand = [random.choice(cards), random.choice(cards)]
        print("Your hand: ", your_hand)
        print("Dealer's hand: ", dealer_hand[0])
        if check_score(your_hand) == 0:
            print("Blackjack! You win!")
            continue
        while check_score(your_hand) < 21:
            hit = input("Do you want to hit or stand? Type 'hit' or 'stand': ")
            if hit == "stand":
                break
            elif hit == "hit":
                your_hand.append(random.choice(cards))
                print("Your hand: ", your_hand)
                if check_score(your_hand) > 21:
                    print("Bust! You lose.")
                    break
            else:
                print("Invalid response. Please type 'hit' or 'stand'.")
                continue
        if check_score(your_hand) > 21:
            continue
        else:
            print("Dealer's hand: ", dealer_hand)
            while check_score(dealer_hand) < 17:
                dealer_hand.append(random.choice(cards))
                print("Dealer's hand: ", dealer_hand)
            if check_score(dealer_hand) > 21:
                print("Dealer busts! You win!")
            elif check_score(your_hand) > check_score(dealer_hand):
                print("You win!")
            elif check_score(your_hand) < check_score(dealer_hand):
                print("You lose.")
            else:
                print("It's a draw.")
            continue

