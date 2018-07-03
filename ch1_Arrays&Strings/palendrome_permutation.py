from collections import Counter
def palendrome_permutation(str):
	#Check if any of the permutation of a STR is a palendrome
	   # ex. Input: "Tact Coa"
	        #Output: "taco cat", "atco cta", .......

    str = str.replace(" ", "").lower()
    #str = str.strip().replace(" ", "").lower()

    # print str
    cntr = Counter(str)
    # print cntr
    if len(str) % 2 == 0:
        for char in str:
            if cntr[char] % 2 != 0:
                return False
        return True
    else:
        odd_counter = 0
        for char in str:
            if cntr[char] %2 != 0:
                odd_counter += 1
                if odd_counter > 1:
                    return False
        return True

# from collections import Counter
# def palendrome_permutation(str):
# 	str = str.replace(" ", "").lower()
# 	dict = Counter(str)
# 	cntr = 0
# 	for key in dict:
# 		if dict[key] % 2 != 0:
# 			cntr += dict[key]
# 	if cntr > 1:
# 		return False
# 	elif cntr == 1 and len(str) % 2 == 0:
# 		return False
# 	else:
# 		return True

print(palendrome_permutation("Tact Coa"))
print(palendrome_permutation('jhsabckuj ahjsbckj'))
print(palendrome_permutation("Tactfo Coaf"))
print(palendrome_permutation('Able was I ere I saw Elba'))
print(palendrome_permutation('no x in nixon'))

print("Falses are here")
print(palendrome_permutation("Tact Coaf"))
print(palendrome_permutation("Tact Coaa"))
print(palendrome_permutation('So patient a nurse to nurse a patient so'))
print(palendrome_permutation('Random Words'))
print(palendrome_permutation('Not a Palindrome'))


