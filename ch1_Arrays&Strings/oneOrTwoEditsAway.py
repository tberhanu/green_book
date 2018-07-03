from collections import Counter
def oneOrTwoEditsAway(str1, str2):
	if abs(len(str1) - len(str2)) > 1:
		return False
	elif len(str1) == len(str2):
		cntr = 0
		for s1, s2 in zip(str1, str2):
			if s1 != s2:
				cntr += 1
				if cntr > 1:
					return False
		return True

	short_str = str1
	long_str = str2
	if len(str1) > len(str2):
		short_str = str2
		long_str = str1

	cntr1 = Counter(short_str)
	cntr2 = Counter(long_str)
	unique_char = ""
	unique_counter = 0
	for char in long_str:
		if cntr1[char] != cntr2[char]:
			unique_char = char
			unique_counter += 1
			if unique_counter > 1:
				return False
	if unique_char + short_str == long_str or short_str + unique_char == long_str:
		return True

	for i in range(len(short_str)):
		fixed_str = short_str[0:i+1] + unique_char + short_str[i+1:]
		if fixed_str == long_str:
			return True
	return False


print(oneOrTwoEditsAway("pale", "ple"))
print(oneOrTwoEditsAway("pales", "pale"))
print(oneOrTwoEditsAway("pale", "bale"))
print(oneOrTwoEditsAway("pale", "bake"))
print(oneOrTwoEditsAway("paler", "balre"))
print(oneOrTwoEditsAway("pale", "pake"))



