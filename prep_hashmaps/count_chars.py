def count_char_occ(string):
	char_dict = {}
	for char in string:
		if char in char_dict:
			char_dict[char] += 1
		else:
			char_dict[char] = 1

	return char_dict


string = input("Please enter a string: ")
result_tab = count_char_occ(string)
char = input("Choose a character to check: ")
if char in string:
	print(f"Character {char} appeared {result_tab[char]} times")
else:
	print("The character is not in string")


