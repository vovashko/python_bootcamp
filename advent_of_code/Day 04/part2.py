with open ('input.txt', 'r') as file:
    data = file.readlines()

def get_score (input_string):

    scratched_numbers = []
    winning_numbers = []
    card_str, numbers_str = input_string.split(':')
    scratched_str, winning_str = numbers_str.split('|')
    scratched_numbers = scratched_str.split(' ')
    winning_numbers = winning_str.split(' ')

    score = [i for i in scratched_numbers if i in winning_numbers]
    score = [num for num in score if num]

    if len(score) <= 0:
        final_score = 0
    else:   
        final_score = len(score)
    return final_score

total_cards = 0

i = 0
number_of_cards = len(data)
pile_of_cards = [1] * number_of_cards
while i < len(data):
    input_string = data[i].strip()
    final_score = get_score(input_string)
    j = final_score
    while j > 0:
        pile_of_cards[i + j] += 1
        j -= 1
    print(f"Pile of cards updated\n")
    total_cards += 1
    pile_of_cards[i] -= 1
    if pile_of_cards[i] == 0:
        i += 1
    
print(f"Total cards: {total_cards}")