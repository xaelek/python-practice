def censor(text, word):
    censor = ""
    for c in word:
    	censor += "*"
    if word in text:
    	text = text.replace(word, censor)

    return text