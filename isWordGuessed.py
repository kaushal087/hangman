##############################################################

def isWordGuessed(secretWord,lettersGuessed):
    for w in secretWord:
        if w not in lettersGuessed:
            return False

    return True
            
##############################################################

secretWord='ppe'
lettersGuessed=['e','i','k','p','r','s']
print isWordGuessed(secretWord,lettersGuessed)


##############################################################    
