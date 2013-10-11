########################################################################################
############## hangman.py ##############################################################

from imports import *

def hangman(secretWord):

    word_length= len(secretWord)
    print "Length of word : " , word_length
    lettersGuessed = ""
    guessLeft = 8
    while(isWordGuessed(secretWord, lettersGuessed) == False and guessLeft > 0 ):

        print"Guessed Word: ", (getGuessedWord(secretWord, lettersGuessed))
        print"Available Letters: ", (getAvailableLetters(lettersGuessed)), "Used letters: ", lettersGuessed
        print "No of Guess left: ", guessLeft 
        letter = raw_input("Enter your Guess: ")
        if letter not in lettersGuessed:
            lettersGuessed=lettersGuessed+letter
            if letter not in secretWord:
                guessLeft = guessLeft - 1
        else:
            print "You have already guessed that letter"
        print ""
    if (isWordGuessed(secretWord, lettersGuessed) == True):
        print "YOU WON!"
        print "No of Guessed used", (8-guessLeft)
    else:
        print "YOU LOSE!"
        print"Guessed Word: ", (getGuessedWord(secretWord, lettersGuessed))
        
    print "Secret Word: ", secretWord
    
#########################################################################################    

