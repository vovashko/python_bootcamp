def unique_char(string):

	char_dict = {}

	for char in string:
		if char not in char_dict:
			char_dict[char] = 1
		
	return char_dict


string = input("Enter a string: ")
result_arr = []
unique_dict = unique_char(string)

print(f"Here are the unique chars: {unique_dict}")

for char, count in unique_dict.items():
	result_arr.append(char)

print(f"here it is as an array: {result_arr}")

result_str = ''.join(result_arr)

print(f"here it is as a string: {result_str}")


