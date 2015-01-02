import nltk
import random
from nltk.corpus import cmudict
from nltk.corpus import words
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
        syllablesNeeded = totalSyllables-lineSyllables
        word = getWordSyllablesLessOrEq(syllablesNeeded)
        # some words in cmudict don't seem to be english words?
        # while word not in set(words.words()):
        #     word = random.choice(cmudict.words())
        line = addWord(line, word)
        lineSyllables += countSyllables(d[word][0])
    return line

def getWordSyllablesLessOrEq(syllableNum):
    word = random.choice(cmudict.words())
    while countSyllables(d[word][0]) > syllableNum:
        word = random.choice(cmudict.words())
    return word

def addWord(line, word):
    line += word + " "
    return line

print buildLine(5)
