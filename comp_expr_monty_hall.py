import random
from enum import Enum, auto


class Door(Enum):
  GOAT = auto()
  CAR = auto()

def selectDoor(values):
  return random.choice(values)

def montyHallStay():
  initialDoor = selectDoor([Door(2).name, Door(1).name, Door(1).name])
  return initialDoor

def switch(door):
  if door == Door(1).name:
    return Door(2).name
  elif door == Door(2).name:
    return Door(1).name

def montyHallSwitch():
  initialDoor = selectDoor([Door(2).name, Door(1).name, Door(1).name])
  switchedDoor = switch(initialDoor)
  return switchedDoor

def enumerate(strategy):
  nSamples = 1000
  return [strategy() for s in range(nSamples)]

def summarize(values):
  return sum([v == Door(2).name for v in values]) / len(values)

if __name__ == '__main__':
  print("Probability of winning if stay: " + str(summarize(enumerate(montyHallStay))))
  print("Probability of winning if switch: " + str(summarize(enumerate(montyHallSwitch))))