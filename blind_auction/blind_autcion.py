print("Welcome to the secret auction program.")
current_bidders = {}
highest_bid = 0
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    current_bidders[name] = bid

    stop = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if stop == "no":
        for bidder in current_bidders:
            if current_bidders[bidder] > highest_bid:
                highest_bid = current_bidders[bidder]
                winner = bidder
        break
    if stop == "yes":
        continue


print(f"The winner is {winner} with a bid of ${highest_bid}")