#Ask the user if they'd like to know how to keep an idiot busy for hours.
#If the user answers 'no', quit.
#If the user answers 'yes', go to step 1.

import pyinputplus as pyip

while True:
    promt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(promt)
    if response == 'no':
        break

print('Thank you. Have a nice day.')

