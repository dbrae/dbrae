import zombiedice, random

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
        
    
class RandomCoinFlipZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        while diceRollResults is not None:
            if random.randint(0, 1) == 0: #randomly decide to stop or continue
                diceRollResults = zombiedice.roll() #roll again
            else:
                break

class TwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['brains']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MoreShotgunsThanBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotguns < brains:
                diceRollResults = zombiedice.roll()
            else:
                break

class OneToFourRollsTwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        shotguns = 0
        rolls = 0
        while diceRollResults is not None: 
            shotguns += diceRollResults['shotgun'] #counting the shotguns
            rolls += 1 #counting the rolls
            if shotguns < 2 and rolls < 4: #if less than 2 shotguns and less than 4 rolls
                diceRollResults = zombiedice.roll() #roll again
            else:
                break

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
    MyZombie(name='My Zombie Bot'),)
        # Add any other zombie players here.)

#uncomment one of the following lines to run in CLI or Web GUI mode
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)