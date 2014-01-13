from math import sqrt

#badly implemented prime checker, need to fix many things

def is_prime(x):
    if x < 2:
        return False
    prime = False
    minPrime = 2
    numberList = list(range(minPrime, x + 1))
    for index in numberList:
        minPrime = index
        while index <= x:
            try:
                numberList.remove(index * minPrime)
            except ValueError:
                pass
            index += 1
    for i in numberList:
        if x != i:
            prime = False
        elif x == i:
            prime = True
    return prime
    
is_prime(100)    
    

#rangeList = list(range(2,101))
#rangeNum = rangeList[0]
#print type(rangeNum)
#print rangeList
#numberedList = []
#for i in range(2, 101):
#    numberedList.append(i)
#listNum = numberedList[0]
#print listNum
#print type(numberedList)
#try:
#   numberedList.remove(index * count)
#except ValueError:
#    pass
#print numberedList