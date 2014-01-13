def anti_vowel(text):
	vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
	tempList = []
	for i in text:
	    if i in vowels:
	        text = text.replace(i, "")
	return text

print anti_vowel("Hello World")