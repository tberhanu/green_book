def check_permutation2(str1, str2):
    dict1 = {}
    dict2 = {}
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        char1 = str1[i]
        dict1[char1] = dict1.setdefault(char1, 0) + 1 #setting 0 as a default value of all keys
        char2 = str2[i]
        dict2[char2] = dict2.setdefault(char2, 0) + 1
    for char in dict1:
    	if char not in dict2.keys():
    		return False
        else:
            if dict1[char] != dict2[char]:
                return False
    return True

print(check_permutation2("strr", "rrst"))
print(check_permutation2("strra", "rarst"))
print(check_permutation2("strcra", "raxrst"))
print(check_permutation2("astrcra", "raxrste"))