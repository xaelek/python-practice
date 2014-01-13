def reverseList(text):
    textList = []
    count = 0
    for c in text:
        textList.append(c)
    for i in textList:
        tempLetter = ""
        tempLetter = textList.pop()
        textList.insert(count, tempLetter)
        count += 1
    txet = "".join(textList)
    return txet
    
#textList = ['a', 'b', 'c']
#tempLetter = ""
#tempLetter = textList.pop()
#textList.insert(0, tempLetter)
#print textList

def reverseString(text):
    for c in text:
        