def urlify_replace_spaces_with2(str, length):
    # print(str.strip())
        
	return str.strip().replace(" ", "%20")
print(urlify_replace_spaces_with2("hello world    Tess", 12))
