with open ('input.txt', 'r') as file:
    data = file.readlines()

answer = 0
first_digit = 0
last_digit = 0
i = 0

while i < len(data):
    
    digits = ''.join([char for char in data[i].strip() if char.isdigit()])
    first_digit = digits[0]
    last_digit = digits[-1]
    answer += int(first_digit) * 10 + int(last_digit)
    i += 1

print(f"Answer: {answer}")


