from entities import *
from TestConfiguration import *
import turtle

test_case=0  ##Change the test case from here##

class Arena():     ## Arena Class##
  def __init__(self, test_case):
    self.test_case = test_case

  def InitializeGraphics(self,config): #Initializes the Turtle Graphics##
    attract = config[0] #All the creatures that are attracted to light
    repel = config[1] #All the creatures that are repelled from light
    lights = config[2]
    self.a = [creature(10,attract.speed) for x in range(attract.count)]
    self.r = [creature(10,repel.speed) for y in range(repel.count)]
    self.l = [light(10,lights.speed) for z in range(lights.count)]
    '''The following lines of code draws every creature and light in the swarm'''
    for x in self.a:
      x.robot.color('red')
      x.draw()
    for y in self.r:
      y.robot.color('blue')
      y.draw()
    for z in self.l:
      z.draw()
    
  
  def Update(self): #Update function that updates the turtle position
    for x in self.a:
      x.move()
      x.draw()
    for y in self.r:
      y.move()
      y.draw()
    for z in self.l:
      z.move()
      z.draw()
      


def main():
  turtle.tracer(0,0)
  arena = Arena(test_case)
  arena.InitializeGraphics(example[test_case]) #Calling the arena class with test case
  try:
    while True:  #keeps updating until broken manually
      arena.Update()    
      turtle.update()
  except KeyboardInterrupt:
    print('Done swarming.')
main()

