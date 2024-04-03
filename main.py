#####################################################################
# author: Blaine Hord
# date: 3/18/2024  
# description: A person class 
#####################################################################
import math
# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Person():
  def __init__(self, name="player 1", x=0, y=0, size=1):
    self.name = name
    self.x = x
    self.y = y
    self.size = size

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    if len(name)>=2: self._name = name
    else: self._name = "player 1"

  @property
  def x(self):
    return self._x
    
  @x.setter
  def x(self, x):
    if (x>=MAX_X): self._x = MAX_X
    elif (x>=0): self._x = x
    else: self._x = 0

  @property
  def y(self):
    return self._y
      
  @y.setter
  def y(self, y):
    if (y>=MAX_Y): self._y = MAX_Y
    elif (y>=0): self._y = y
    else: self._y = 0

  @property
  def size(self):
    return self._size

  @size.setter
  def size(self, size):
    if size >= 1: self._size = size
    else: self._size = 1

  #A Person can goLeft. This will reduce the x value of a Person by the provided value. If the value is not provided, the x value is reduced by 1.
  def goLeft(self, x=1):
    self.x -= x

  def goRight(self, x=1):
    self.x += x

  def goUp(self, y=1):
    self.y -= y

  def goDown(self, y=1):
    self.y += y

  def getDistance(self, Person):
    return math.sqrt((self._x - Person._x)**2 + (self._y - Person._y)**2)

  def __str__(self):
    return f"Person({self._name}):, Size = {self._size}, x = {self._x}, y = {self._y}"

# Create some people
p1 = Person()
p2 = Person("John Doe")
p3 = Person("Jane Doe", 3)
p4 = Person("James Doe", 4, 67)
p3.size = 5
p4.size = 15

print("-" * 60)
print("--People with correct inputs--")
print(f"p1:{p1}")
print(f"p2:{p2}")
print(f"p3:{p3}")
print(f"p4:{p4}")

# Creating some people with wrong input values
p5 = Person("a")
p6 = Person("b", 1000, -600)
p7 = Person("c", -12, 1000)
p7.size = -10

print("-" * 60)
print("--People with wrong inputs--")
print(f"p5:{p5}")
print(f"p6:{p6}")
print(f"p7:{p7}")

# Testing some of the other functions
for i in range(10):
    p1.goLeft()
    p2.goRight()
    p3.goUp()
    p4.goDown()

print("-" * 60)
print("--Testing basic movement--")
print(f"p1:{p1}")
print(f"p2:{p2}")
print(f"p3:{p3}")
print(f"p4:{p4}")
print("-" * 60)
print("--Testing Distance measurement--")
print(f"The distance between p1 and p2 is {p1.getDistance(p2)}")
print(f"The distance between p1 and p3 is {p1.getDistance(p3)}")
print(f"The distance between p1 and p4 is {p1.getDistance(p4)}")
print("-" * 60)

for i in [12, 34, 89, -56, 3]:
    p1.goRight(i)
    p2.goLeft(i)
    p3.goDown(i)
    p4.goUp(i)

print("--Testing more movement--")
print(f"p1:{p1}")
print(f"p2:{p2}")
print(f"p3:{p3}")
print(f"p4:{p4}")
print("-" * 60)
print("--Testing Distance measurement--")
print(f"The distance between p1 and p2 is {p1.getDistance(p2)}")
print(f"The distance between p1 and p3 is {p1.getDistance(p3)}")
print(f"The distance between p1 and p4 is {p1.getDistance(p4)}")
print("-" * 60)

# Testing extreme movement
for i in [200, -500, 700, -1200, 3000]:
    p1.goRight(i)
    p2.goLeft(i)
    p3.goDown(i)
    p4.goUp(i)

print("--Testing extreme movement--")
print(f"p1:{p1}")
print(f"p2:{p2}")
print(f"p3:{p3}")
print(f"p4:{p4}")
print("-" * 60)
print("--Testing Distance measurement--")
print(f"The distance between p1 and p2 is {p1.getDistance(p2)}")
print(f"The distance between p1 and p3 is {p1.getDistance(p3)}")
print(f"The distance between p1 and p4 is {p1.getDistance(p4)}")
print("-" * 60)
