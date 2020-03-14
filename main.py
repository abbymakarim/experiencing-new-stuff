import random

class Player:

  def __init__(self, name, gameclass):
    self.name = name
    self.gameclass = gameclass
    if gameclass == 'Warrior':
      self.health = 10
      self.attack = 2
    elif gameclass == 'Knight':
      self.attack = 3
      self.health = 8

  def __str__(self):
    return "Name: " + self.name + "\nClass: " + self.gameclass + "\nCurrent Health: " + str(self.health)

  def attack_player(self, another_player):
    print(self.name + " Attack " + another_player.name)
    another_player.set_health(another_player.health - self.attack)

  def set_health(self, health):
    self.health = health

  
  
#Main Menu
while True:
    print('Hello, Welcome to an RPG Game')
    print('Play \nQuit')
    playGame = input()
    if playGame == 'Play':
        print('What is your name hero?')
        name = input()
        gameclass = ""
        while gameclass != 'Warrior' and gameclass != 'Knight':
          print('Tell me ' + str(name) + ', what are you? \nWarrior \nKnight')
          gameclass = input()
        player = Player(name, gameclass)
        player2 = Player("Computer", "Knight")

        player.attack_player(player2)

        print(player)
        print(player2)
    elif playGame == 'Quit':
        print('Thanks for Playing!')
    else:
        continue
    break