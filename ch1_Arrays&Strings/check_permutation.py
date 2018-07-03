def check_permutation(str1, str2):
	if len(str1) != len(str2):
		return False
	for char1 in str1:
		if char1 not in str2:
			return False
		else:
			for char2 in str2:
				if char1 == char2:
					str2 = str2.replace(char2, "", 1) #replace only one matched char, not all matched chars
					break
	return True

print(check_permutation("stsr", "rtss"))