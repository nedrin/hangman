"""
Hangman

Created by Alessandro - 23/08/2018
Editted by Kevin

"""

import random
import time

words= ["the","graphics","for","hangman","are","keyboard","characters","printed" ,"on","the","screen"]
picker = len(words) - 1
start = ""
wordToGuess = ""
userLetter = ""
dead = 8
guessedLetters = []
correctLetters = []
wordCount = len(wordToGuess)
guessedCount = 0

def welcomeText():
    #Welcome text, printed at start of game.
    
    print("Welcome to hangman, the word guessing game.")

def startGame():
    #Game initializer
    
    print("Would you like to start the game? (Y)es, (N)o")
    global start
    start = input().lower()

    
def grabWord():
    #Grabs a random word from the words list
    
    global wordToGuess
    wordToGuess = words[random.randint(0, picker)]

def wordGuess():
    # Checks if the word has already been guessed, if True asks again, if not it adds the letter to the
    # guessed library.


    
    global userLetter
    global guessedLetters

    userLetter = input("\nPlease input a single letter: ").lower()
    if len(userLetter) > 1:
        print("You've entered more than 1 letter.... \n")
        time.sleep(1)
        wordGuess()
    
    
    if userLetter in guessedLetters:
        print("You already tried that letter, pick another one...")
        time.sleep(1)
        wordGuess()
    elif userLetter in wordToGuess:
        correctLetters.append(userLetter)
        guessedLetters.append(userLetter)   

    else:
        guessedLetters.append(userLetter)   

def wordDisplay():
    global wordToGuess
    for letter in wordToGuess:
        if letter in correctLetters:
            print(letter.upper(), end =" ")
        else:
            print("_", end=" ")

def wordCheck():
    global wordToGuess
    global guessedLetters
    global guessedCount
    global wordCount
    global correctLetters
    global start
    
    for letter in wordToGuess:
        if letter in correctLetters:
            guessedCount += 1
            if guessedCount == wordCount:
                print("Guessed all letters of the word " + wordToGuess.upper())
                print("Ending Game")
                start = "n"
            
                
            
                
    
    
startGame()
grabWord()
wordCount = len(wordToGuess)
welcomeText()
if start != "y":
    print("Ok than....")

while start == "y":
    time.sleep(1)
    print("Your word: \n ",end="")
    wordDisplay()
    time.sleep(1)
    wordGuess()
    guessedCount = 0
    if userLetter in wordToGuess:
        print("Correct")
        wordCheck()
        
        
    else:
        print("You have " + str(dead - 1) + " tries left.")
        dead -= 1
        if dead == 0:
            print("You've died.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            start = input("Would you like to play again? (Y)es, (N)o")
            picker = len(words) - 1
            wordToGuess = ""
            userLetter = ""
            dead = 8
            guessedLetters = []
            grabWord()
            welcomeText()
            
            
        

    
