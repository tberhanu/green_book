def urlify_replace_spaces_with(str, length):
	space_taker = "%20"
	filled_str = ""
	for char in str:
		if char == " ":
			filled_str += space_taker 
		else:
			filled_str += char
	return filled_str



print(urlify("hello world   Tess", 18))




