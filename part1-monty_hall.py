import random
from enum import Enum, auto
import numpy as np


class Door(Enum):
  GOAT = auto()
  CAR = auto()

class Strategy(Enum):
  STAY = auto()
  SWITCH = auto()

def generateGame():
  game = [Door(1).name, Door(1).name, Door(2).name]
  random.shuffle(game)
  return game

def playGame(strategy):
  game = generateGame()
  initialDoor = random.randrange(3)
  
  hostDoor = random.choice(
    [i for i in [0, 1, 2] if (i != initialDoor) and (game[i] != Door(2).name)]
  )

  switchedDoor = [i for i in [0, 1, 2] if (i != initialDoor) and (i != hostDoor)][0]

  if strategy == Strategy(1).name:
    return (game[initialDoor] == Door(2).name)
  elif strategy == Strategy(2).name:
    return (game[switchedDoor] == Door(2).name)

if __name__ == '__main__':
  nSamples = 1000

  ifStay = np.mean([playGame(Strategy(1).name) for i in range(nSamples)])
  ifSwitch = np.mean([playGame(Strategy(2).name) for i in range(nSamples)])

  print("Probability of winning if stay: " + str(ifStay))
  print("Probability of winning if switch: " + str(ifSwitch))

