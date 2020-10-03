def cont():
    while True:
        question = input("Keep Gaming? ")
        question = fixword(question)
        if question in {"yessir", "yessiryessir", "yessuh", "y", "yes"}:
            break
        elif question in {"n", "no"}:
            exit("Goodbye!")
        else:
            print("Must be a yes or no response.")

def diction():
    with open('engmix.txt', 'r', encoding='latin-1') as realwords:
        realset = set(realwords.read().split())
    return realset

def fixword(word):
    word = word.replace('.', '')
    word = word.replace(':', '')
    word = word.replace(';', '')
    word = word.replace('!', '')
    word = word.replace('?', '')
    word = word.replace(' ', '')
    word = word.lower()
    return word

def generatewords(maxlength):
    from random import choice, sample
    fullwords = []
    dictionary = diction()
    for word in dictionary:
        if len(word) == maxlength:
            fullwords.append(word)
    letters = choice(fullwords)
    letters = ''.join(sample(letters,len(letters)))
    words = stringsubsets(letters, 3, maxlength)
    return letters, words

def randstring(length):
    from string import ascii_lowercase
    from random import choice
    alphabet = list(ascii_lowercase)
    retstring = ""
    letters = 0
    while letters < length:
        retstring += choice(alphabet)
        letters += 1
    return retstring

def stringsubsets(string, start, stop):
    from itertools import permutations
    from functools import reduce
    from operator import add

    substrings = []
    subsfix = []
    dictionary = diction()
    for num in range (start, stop+1):
        subsraw = list(permutations(string, num))
        for i in subsraw:
            subsfix.append(''.join(i))
        for sub in subsfix:
            if sub not in substrings: 
                if sub in dictionary:
                    substrings.append(sub)
    return substrings