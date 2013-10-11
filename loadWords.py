###########################################################################################
########################## loadWords.py ###################################################
from imports import *

def loadWords():
    WORDLIST_FILENAME = "words.txt"
    
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    return wordlist

###########################################################################################

