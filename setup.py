#################### setup.py ###################################
## this is where the game starts ################################

from imports import *

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

##################################################################
