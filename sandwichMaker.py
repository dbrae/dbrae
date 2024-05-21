import pyinputplus as pyip

#using inputMenu() for a bread type: wheat, white, sourdough
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)

#using inputMenu() for a protein type: chicken, turkey, ham, tofu
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)

#using inputYesNo() to ask if they want cheese
cheese = pyip.inputYesNo('Do you want cheese?')

#if so, using inputMenu() to pick a cheese type: cheddar, Swiss, mozzarella
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)

#using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato
mayo = pyip.inputYesNo('Do you want mayo?')
mustard = pyip.inputYesNo('Do you want mustard?')
lettuce = pyip.inputYesNo('Do you want lettuce?')
tomato = pyip.inputYesNo('Do you want tomato?')

#using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
sandwiches = pyip.inputInt('How many sandwiches do you want?', min=1)

#come up with prices for each of these options, and have your program display a total cost after the user enters their selection.

