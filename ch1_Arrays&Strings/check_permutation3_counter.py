from collections import Counter

def check_permutation3_counter(str1, str2):
	if len(str1) != len(str2):
		return False

	cntr1 = Counter(str1) #gives a dictionary of each CHAR:FREQUENCY
	cntr2 = Counter(str2)
	for key1 in cntr1:
		for key2 in cntr2:
			if key1 == key2 and cntr1[key1] != cntr2[key2]:
				return False
			elif key1 == key2 and cntr1[key1] == cntr2[key2]:
				break
	
	return True


	print(cntr1)
	print(cntr2)
print(check_permutation3_counter("hello", "ohhhh"))
print(check_permutation3_counter("strr", "rrst"))
print(check_permutation3_counter("strra", "rarst"))
print(check_permutation3_counter("strcra", "raxrst"))
print(check_permutation3_counter("astrcra", "raxrste"))