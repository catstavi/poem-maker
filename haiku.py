import nltk
import random
from nltk.corpus import cmudict
d = cmudict.dict()

def hasNumber(strInput):
    return any(char.isdigit() for char in strInput)

def countSyllables(phonemeList):
    syllableCount = 0
    for x in range(0, len(phonemeList)):
        if hasNumber(phonemeList[x]):
            syllableCount += 1
    return syllableCount

def buildLine(totalSyllables):
    line = ""
    lineSyllables = 0
    while lineSyllables < totalSyllables:
        word = random.choice(cmudict.words())
        line = addWord(line, word)
        lineSyllables += countSyllables(d[word][0])
    return line

def addWord(line, word):
    line += word + " "
    return line

# line1 = buildLine(5)
print buildLine(5)
