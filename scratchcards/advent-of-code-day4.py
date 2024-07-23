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
        final_score = pow(2, len(score) - 1)
    print(f"Final score for {card_str}: {final_score}")
    return final_score

total_final_score = 0

i = 0
while i < len(data):
    input_string = data[i].strip()
    final_score = get_score(input_string)
    total_final_score += final_score
    i += 1
    
print(f"Total final score: {total_final_score}")