# Works the same as the iMessage version of this game
# Will always allow for at least one six letter word

from AnagramFunctions import cont, fixword, generatewords
import time

gametime = int(input("How long would you like each round of this game to last? (number of seconds) "))
while True:
    maxlength = int(input("How many letters would you like to play with? (number) "))
    letters, words = generatewords(maxlength)                               # Gives a list of maxlength letters and the words that can be made from them
    pointlist = [100, 400, 1200, 2000]                              # Specified point values for 3, 4, 5, and 6 letter words respectively
    starttime = time.time()             
    currenttime = time.time()                                                   
    pointtotal = 0
    correctwords = []
    while (currenttime - starttime) < gametime:
        guess = str(input("Guess words with these letters: " + letters + " "))
        guess = fixword(guess)
        if guess in words:
            if guess not in correctwords:                           # Ensures the user cannot enter the same word multiple times
                correctwords.append(guess)
                points = pointlist[len(guess)-3]
                print(guess + " is one of the words! You recieved " + str(points) + " points!")
                pointtotal += points
            else:
                print("You have already guessed this word!")
        else: 
            print("That is not a word.")
        currenttime = time.time()                                   # Refreshes to check if the user has run out of time after each guess
    print("\nGame Over!")
    print("You scored " + str(pointtotal) + " total points with the following words:")
    print(correctwords)
    print("These were all the possible words: ")
    print(words)
    if pointtotal == 6900:
        print("Nice score btw")
    cont()