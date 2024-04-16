#Write a function that uses regular expressions to make sure the password string it is passed is strong. 
#A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. 
#You may need to test the string against multiple regex patterns to validate its strength.

import re

def strongPasswordDetection(password):
    # Regex pattern that checks:
    # - at least 8 characters
    # - at least one uppercase letter
    # - at least one lowercase letter
    # - at least one digit
    # This pattern allows for characters beyond alphanumeric to support stronger security practices if desired.
    pattern = re.compile(
        r'^(?=.*[A-Z])'  # at least one uppercase letter
        r'(?=.*[a-z])'   # at least one lowercase letter
        r'(?=.*[0-9])'   # at least one digit
        r'.{8,}$'        # at least 8 characters in total
    )
    return bool(pattern.search(password))

# Example usage
password = 'Password123'
print(strongPasswordDetection(password))  # Output should be True if the password meets the criteria
