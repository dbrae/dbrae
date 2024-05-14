#Ask the user if they'd like to know how to keep an idiot busy for hours.
#If the user answers 'no', quit.
#If the user answers 'yes', go to step 1.

import pyinputplus as pyip

while True:
    promt = 'Vous voulez savoir comment occuper un idiot pendant des heures?\n'
    response = pyip.inputYesNo(promt, yesVal='oui', noVal='non')
    if response == 'non':
        break

print('Thank you. Have a nice day.')

