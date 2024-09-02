# Time complexity:


def zero_sum(arr):
	num_tab = {}

	pairs = 0

	for num in arr:
		if num in num_tab:
			num_tab[num] += 1
		else:
			num_tab[num] = 1


	for num, count in num_tab.items():
		if num > 0 and -num in num_tab:
			while count > 0 and num_tab[-num] > 0:
				pairs += 1
				count -= 1
				num_tab[-num] -= 1
		elif num == 0 and count > 1:
			while count > 0:
				pairs += 1
				count -= 2
		
	return pairs



arr = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]


print(f"the result is: {zero_sum(arr)}")


arr = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]

print(f"the result is: {zero_sum(arr)}")

arr = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]

print(f"the result is: {zero_sum(arr)}")

arr = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]

print(f"the result is: {zero_sum(arr)}")


# time elapsed 30 minutes