## HANGMAN GAME - Text based version
# assumes that the player will follow all rules/inputs

import os.path
from os import path
import random

## DEFINE FUNCTIONS
# Add word to hangmanWords file
def addWord(word):
    words = open("hangmanWords.txt", "a+")
    words.write(word.lower() + ",")
    words.close()

def addWords():
    addMore = "Y";
    while addMore == "Y":
        word = input("Please add a word to the list of words: ")
        addWord(word)
        addMore = input("Would you like to add more words? (Y/N): ")
    gameChoice()

# Get list of words from hangmanWords file
def getWords():
    words = open("hangmanWords.txt", "r")
    contents = words.read().split(",") #last item will always be an empty one
    return contents

# Get a random word for the game
def selectWord():
    contents = getWords()
    position = random.randint(0, len(contents)-2)
    return contents[position]

# Make decision to start the game
def gameChoice():
    choice = input("Would you like to start a round (1), add words (2), or exit (other)?: ")
    if choice == "1":
        startGame()
    elif choice == "2":
        addWords()
    else:
        print("Thank you for playing. The game will now end.")

# Actual gameplay here
def startGame():
    TURNS_ALLOWED = 6
    word = selectWord()
    playerKnows = ""
    for char in word:
        playerKnows += "_"
    playerKnows = list(playerKnows)
    turnsTaken = 0
    victory = False

    print("Starting the game now.")
    print("Here is the word as you know it" + " ".join(playerKnows))
    print("You have", TURNS_ALLOWED-turnsTaken, "turns left.")
    
    while (turnsTaken < TURNS_ALLOWED) & (~victory):
        letter = input("Input a letter: ")
        if letter.lower() in word:
            index = 0
            for char in word:
                if char == letter:
                    playerKnows[index] = letter.lower() #strings are immutable
                index += 1
        else:
            turnsTaken += 1
       
    
        if "_" in playerKnows:
            print("You have", TURNS_ALLOWED-turnsTaken, "turns left.")
            print("The word known so far is " + " ".join(playerKnows))
        else:
            victory = True
            
    if victory:
        print("You won!! It was "+ word + "!")
    else:
        print("Too bad. Try again next time.")

    gameChoice()

## START GAME
if path.exists("hangmanWords.txt"):
    gameChoice()    
else:
    addWords()




    


