from collections import Counter
def string_compression(string):
	cntr = Counter(string)
	prev = string[0] 
	compressed_str = prev + str(cntr[prev])

	for s in string[1:]:
		if s != prev:
			compressed_str = compressed_str + s + str(cntr[s])
			prev = s
	if len(compressed_str) >= len(string):
		return string
	else:
		return compressed_str

print(string_compression("aabbbccccddddd"))
print(string_compression("abcde"))
print(string_compression("abbc"))


		
