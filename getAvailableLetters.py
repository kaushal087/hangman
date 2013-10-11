###########################################################################
from imports import *


def getAvailableLetters(lettersGuessed):
    result=""
    for w in string.ascii_lowercase:
        if w not in lettersGuessed:
            result=result+w
    return result

##########################################################################
############## test case #################################################
# lettersGuessed=['e','i','k','p','r','s']

# print getAvailableLetters(lettersGuessed)
    
##########################################################################
