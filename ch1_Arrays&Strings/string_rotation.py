def string_rotation(str1, str2):
	if len(str1) != len(str2):
		return False
	else:

		return is_substring(str1 + str1, str2)

def is_substring(string, sub):
    return string.find(sub) != -1


print(string_rotation("waterbottle", "erbottlewat"))
print(string_rotation("waterbottle", "erbottlewao"))
print(string_rotation("waterbottle", "erbottle"))

print(is_substring("waterbottle", "erbottlewao"))
print(is_substring("waterbottle", "erbottlewat"))
print(is_substring("waterbottle", "erbottle"))
