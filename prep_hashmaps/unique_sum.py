def unique_sum (arr):
	number_tab = {}

	for number in arr:
		if number in number_tab:
			number_tab[number] += 1
		else:
			number_tab[number] = 1

	unique_tab = []

	for number, count in number_tab.items():
		unique_tab.append(number)

	return unique_tab

array = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]

new_array = unique_sum(array)

print(f"The array looks like this: {new_array}")

result = 0

for element in new_array:
	result += element

print(f"The result is: {result}")


array = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]

new_array = unique_sum(array)

print(f"The array looks like this: {new_array}")

result = 0

for element in new_array:
	result += element

print(f"The result is: {result}")



#time elapsed 15 minutes