def isUnique(str):
	dict = {}
	for char in str:
		if char in dict:
			return False
		dict[char] = True
	return True
# Without data structure
def is_unique2(string):
	for i  in range(len(string)):
		for j in range(i + 1, len(string)):
			a = string[i]
			b = string[j]
			if a == b:
				return False
	return True

a = "ssaaa"
b = "sak"
print(is_unique2(a))
print(is_unique2(b))
print(isUnique("string"))
print(isUnique("stringg"))