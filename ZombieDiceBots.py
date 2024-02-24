#! python3
#Zombie Dice Bots

import zombiedice

class MyZombie:
    def __init__(self, name):
        #All zombies must have a name
        self.name = name

    def turn(self, gameState):
        #gameState is a dict with info about the current state of the game
        #You can choose to ignore it in your code
        diceRollResults = zombiedice.roll() #first roll
        #roll() returns a dictionary with keys 'brains', 'shotgun', and 'footsteps'
        #The values are the number of each rolled
        #The 'rolls' key is a list of (color, result) tuples with the exact roll results
        #e.g. ('green', 'brains'), ('red', 'shotgun'), ('yellow', 'footsteps')
        #replace the code here with your strategy
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
    
    zombies = (
        zombiedice.examples.RandomCoinFlipZombie(name='Random'),
        zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
        zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
        zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
        MyZombie(name='My Zombie Bot'),
        # Add any other zombie players here.
    )

    #uncomment one of the following lines to run in CLI or Web GUI mode
    #zombiedice.runTournament(zombies=zombies, numGames=1000)
    zombiedice.runWebGui(zombies=zombies, numGames=1000)