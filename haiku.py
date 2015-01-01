import nltk
import random
from nltk.corpus import cmudict

def hasNumber(strInput):
    return any(char.isdigit() for char in strInput)

d = cmudict.dict()
w1 = random.choice(cmudict.words())
syllableCount = 0
print w1
for x in range(0, len(d[w1][0])):
    # print d[w1][0][x]
    if hasNumber(d[w1][0][x]):
        syllableCount += 1

print syllableCount
