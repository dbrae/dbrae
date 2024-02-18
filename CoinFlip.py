create a list that looks like T T T T H H H H TH H TH H TH
flip it 100 times
find out how often a streak of 6 heads or a streak of 6 tails coes up in a randomly gen list of heads and tailsbreak up experimet into two parts
first part gens list of randomly selected heads and tails values and the second checks if there is a streak in itput in a loop that repeats 10000 times.
function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 the other 50% o the time

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    # Code that checks if there is a streak of 6 heads or tails in a row.
    coinFlip = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            coinFlip.append('H')
        else:
            coinFlip.append('T')
            
        
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
