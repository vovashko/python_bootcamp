def are_anagrams(str1, str2):
	
	if len(str1) != len(str2):
		return False
	
	all_chars = {}

	for char in str1: 
		if char in all_chars:
			all_chars[char] += 1
		else:
			all_chars[char] = 1

	for char in str2:
		if char in all_chars:
			all_chars[char] -= 1
		else:
			return False
		

	for count in all_chars.values():
		if count != 0:
			return False
	return True


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = are_anagrams(str1, str2)
print(f"The strings are anagrams: {result}")