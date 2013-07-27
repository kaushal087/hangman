#########################################################################

def getGuessedWord(secretWord,lettersGuessed):
    printWord=""
    for w in secretWord:
        if w in lettersGuessed:
            printWord=printWord+w
        else:
            printWord=printWord+" _ "
    return printWord

#########################################################################

secretWord='apple'
lettersGuessed=['e','i','k','p','r','s']

print secretWord
print getGuessedWord(secretWord,lettersGuessed)

########################################################################
