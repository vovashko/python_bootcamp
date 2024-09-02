def can_be_pal(string):
	char_count = {}

	for char in string:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1

	flag = 0

	for count in char_count.values():
		if count % 2 != 0:
			flag += 1

	
	if flag > 1:
		return False
	return True




stor = input("Enter string to check: ")

print(f"The string can be palindrome: {can_be_pal(stor)}")