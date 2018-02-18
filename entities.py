import turtle
import random
import math
from TestConfiguration import *
##draws the area for the swarm to move in##
turtle.speed(0)
turtle.pu()
turtle.goto(-250,-250)
turtle.left(90)
turtle.pd()
turtle.hideturtle()
for count in range(4):
  turtle.forward(500)
  turtle.right(90)
## END ##
  
class Position :
  # A data structure to conveniently hold an x,y position
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
class thing: # The base class which gives the base to creature and light child classes
    def __init__(self,radius,speed):
      self.radius = radius
      self.heading =  math.radians(random.randint(-180,180))
      self.position = Position(random.randint(-250,250),random.randint(-250,250))
      self.robot=turtle.Turtle()
      self.speed = speed
        
    def move(self):
      
      if (self.position.x >= 250 or self.position.x <= -250) or (self.position.y >= 250 or self.position.y <= -250) : ##This condition keeps all the animals in the swarm##
        if (self.position.x >= 250 or self.position.x <= -250):
          self.heading = DetermineNewHeading([self.position, self.heading, self.speed],Position(250,self.position.y))
        else:
          self.heading = DetermineNewHeading([self.position, self.heading, self.speed],Position(self.position.x,250))
          
        distance = self.speed
        deltaX = distance*math.cos(self.heading)
        deltaY = distance*math.sin(self.heading)
        self.position.x += deltaX
        self.position.y += deltaY
      else:
        distance = self.speed
        deltaX = distance*math.cos(self.heading)
        deltaY = distance*math.sin(self.heading)
        self.position.x += deltaX
        self.position.y += deltaY

       
class creature(thing): ## This is the child class which creates multiple objects that are animals
  
  def __init__(self,radius,speed):
      thing.__init__(self,radius,speed)

  def draw(self):  #This draws a creature
    self.robot.clear()
    self.robot.hideturtle()
    self.robot.penup()
    self.robot.goto(self.position.x, self.position.y)
    self.robot.dot(self.radius*1.5)
    deltaX = self.radius*math.cos(self.heading)
    deltaY = self.radius*math.sin(self.heading)
    self.robot.goto(self.position.x+deltaX,self.position.y+deltaY)
    self.robot.dot(self.radius*.65)


class light(thing): ## Child class for lights
  def __init__(self,radius,speed):
    thing.__init__(self,radius,speed)

  def draw(self):
    self.robot.clear()
    self.robot.color('yellow')
    self.robot.hideturtle()
    self.robot.penup()
    self.robot.goto(self.position.x, self.position.y)
    self.robot.dot(self.radius*1.5)
    deltaX = self.radius*math.cos(self.heading)
    deltaY = self.radius*math.sin(self.heading)

''' The following code was provided and has been used as instructed'''
# This does assume that the two balls are not overlapping.
# See flatredball if you want to reposition
# them to be touching, but not overlapping position

def Velocity(angle, length):
  x = length*math.cos(angle)
  y = length*math.sin(angle)
  return Vector(x,y)

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.angle = math.atan2(y,x)


# The call might look like this, where "c" and "c2" are instantiations
# of creatures
# h=collision.DetermineNewHeading( \
#   [c.position, c.heading, c.speed], c2.position)
#
# Or if it is a wall - specifically the right wall, like this ...
# h = collision.DetermineNewHeading( \
#  [self.position, self.heading, self.speed],
#  Position(MAX_XPOS,self.position.y))

# The stationary would be a wall or another creature.
# Code can be adjusted for 2 moving creatures, but not necessary
def DetermineNewHeading( creature, stationary_pos ):
  # creature = [ position, heading, speed ]
  # stationary = position
  creature_vel = Velocity(creature[1],creature[2])
  
  # Determine the point of collision, which also defines the angle
  collision = Vector( stationary_pos.x-creature[0].x, \
                      stationary_pos.y-creature[0].y )

  # Define the tangent to the point of collision
  collision_tangent = Vector( stationary_pos.y-creature[0].y, \
                              -(stationary_pos.x-creature[0].x))

  # Normalize the tangent making it length 1
  tangent_length = (collision_tangent.x**2 + collision_tangent.y**2)**0.5
  normal_tangent = Vector( collision_tangent.x/tangent_length, \
                           collision_tangent.y/tangent_length)

  # relative velocity = robot because stationary circle has 0 velocity
  # See flatredball to modify code for 2 moving objects
  rel_velocity = creature_vel

  # Determine the velocity vector along the tangent
  length = rel_velocity.x*normal_tangent.x + rel_velocity.y*normal_tangent.y
  tangent_velocity = Vector( normal_tangent.x*length, normal_tangent.y*length)

  # Determine the velocity vector perpendicular to the tangent
  perpendicular = Vector(rel_velocity.x-tangent_velocity.x, \
                         rel_velocity.y-tangent_velocity.y )

  # New Heading
  # This is for robot only. See flatredball to move both entities
  new_heading = Vector( (creature_vel.x-2*perpendicular.x), \
                        (creature_vel.y-2*perpendicular.y))

  return new_heading.angle
