with open ('example.txt', 'r') as file:
    data = file.readlines()

answer = 0
first_digit = 0
last_digit = 0
i = 0

spelled_digits = {'one' : '1',
                    'two' : '2',
                    'three' : '3',
                    'four' : '4',
                    'five' : '5',
                    'six' : '6',
                    'seven' : '7',
                    'eight' : '8',
                    'nine' : '9'}




while i < len(data):
    for spelled, digit in spelled_digits.items():
        data[i] = data[i].replace(spelled, digit)
    digits = ''.join([char for char in data[i].strip() if char.isdigit()])
    print(digits)
    first_digit = digits[0]
    last_digit = digits[-1]
    answer += int(first_digit) * 10 + int(last_digit)
    i += 1

print(f"Answer: {answer}")


