import random

def characterIntro():
    characterName = ''
    print('What is your name hero?')
    characterName = input()
    return characterName


def characterSel():
    while True:
        characterClass = ''
        print('Tell me ' + str(Name) + ', what are you? \nWarrior \nKnight')
        characterClass = input()
        if characterClass == 'Warrior' or characterClass == 'Knight':
            return characterClass
        else:
            continue


def characterStats():
    characterHealth = ''
    if Class == 'Warrior':
        print('You are a Warrior!')
        characterHealth = 10
        print('What armour do you choose? (Iron or Gold?)')
        armourPicked = ''
        armourCurrent = ''
        armourPicked = input()
        if armourPicked == 'Iron':
            armourCurrent = random.randint(1, 4)
        elif armourPicked == 'Gold':
            armourCurrent = random.randint(2, 3)
        print('You chose ' + armourPicked + ' armour!')
    elif Class == 'Knight':
        print('You are a Knight!')
        characterHealth = 8
        print('What armour do you choose? (Steel or Metal?)')
        armourPicked = ''
        armourCurrent = ''
        armourPicked = input()
        if armourPicked == 'Steel':
            armourCurrent = random.randint(3, 8)
        elif armourPicked == 'Metal':
            armourCurrent = random.randint(4, 7)
        print('You chose ' + armourPicked + ' armour!')

#Main Menu
while True:
    print('Hello, Welcome to an RPG Game')
    print('Play \nQuit')
    playGame = input()
    if playGame == 'Play':
        Name = characterIntro()
        Class = characterSel()
        characterStats()
    elif playGame == 'Quit':
        print('Thanks for Playing!')
    else:
        continue
    break
