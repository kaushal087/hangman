import random
import string

###########################################################################################

WORDLIST_FILENAME = "words.txt"

###########################################################################################

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """

    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    return wordlist

###########################################################################################

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

##########################################################################################

wordlist = loadWords()

##########################################################################################

def isWordGuessed(secretWord,lettersGuessed):
    for w in secretWord:
        if w not in lettersGuessed:
            return False

    return True
            
#########################################################################################

def getGuessedWord(secretWord,lettersGuessed):
    printWord=""
    for w in secretWord:
        if w in lettersGuessed:
            printWord=printWord+w
        else:
            printWord=printWord+" _ "
    return printWord

#########################################################################################

def getAvailableLetters(lettersGuessed):
    result=""
    for w in string.ascii_lowercase:
        if w not in lettersGuessed:
            result=result+w
    return result
    
########################################################################################

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
        print "No of Guessed wasted : ", (8-guessLeft)
    else:
        print "YOU LOSE!"
        print"Guessed Word: ", (getGuessedWord(secretWord, lettersGuessed))
        
    print "Secret Word: ", secretWord
    
#########################################################################################    

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

#########################################################################################

# END OF THE PROGRAM

#########################################################################################
