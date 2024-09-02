def first_occurance_in_string(string):

	char_dict = {}

	for char in string:
		if char not in char_dict:
			char_dict[char] = 1

	result = []

	for char, count in char_dict.items():
		result.append(char)

	return ''.join(result)


# tests

string = "abracadabra"

print(f"Characters in the string: {first_occurance_in_string(string)}")

string = "Uber Career Prep"

print(f"Characters in the string: {first_occurance_in_string(string)}")

string = "zzyzx"

print(f"Characters in the string: {first_occurance_in_string(string)}")


# time elapsed 8 minutes