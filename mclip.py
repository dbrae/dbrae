#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

# To create a batch file to run the program, create a new file with the following content and save it with a .bat file extension:
# @py.exe C:\path\to\mclip.py %*
# @pause
# If you don’t include the @pause line, the command line window will close as soon as the program finishes running, and you won’t be able to see the output.
# You can also run the program from the command line by typing mclip.py and the keyphrase.
# For example, to copy the upsell text to the clipboard, you would type the following command into the command line:
# mclip.py upsell