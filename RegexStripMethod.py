#Regex Version of the strip() Method
#Write a function that takes a string and does the same thing as the strip() string method.
#If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string.

import re

def regex_strip(string, chars=None):
    if chars is None:
        strip_regex = re.compile(r'^\s+|\s+$')
    else:
        chars = re.escape(chars)
        strip_regex = re.compile(f'^[{chars}]+|[{chars}]+$')
    return strip_regex.sub('', string)


print(regex_strip('  Hello, World!  '))
#Otherwise, the characters specified in the second argument to the function will be removed from the string.
print(regex_strip('SpamSpamBaconSpamEggsSpamSpam', 'ampS'))




