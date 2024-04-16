#Write a function that uses regular expressions to make sure the password string it is passed is strong. 
#A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. 
#You may need to test the string against multiple regex patterns to validate its strength.

import re

def strongPasswordDetection(password):
    #at least 8 characters long
    if len(password) < 8:
        return False
    #contains both uppercase and lowercase characters
    upperCaseRegex = re.compile(r'[A-Z]')
    lowerCaseRegex = re.compile(r'[a-z]')
    #has at least one digit


