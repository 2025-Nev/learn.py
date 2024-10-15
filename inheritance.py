from party import PartyAnimal

class CricketFan(PartyAnimal):

   def __init__(self, nam) :
       super().__init__(nam)
       self.points = 0

   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))

'''
Glossary
attribute
A variable that is part of a class.
class
A template that can be used to construct an object. Defines the attributes and methods that will make up the object.
child class
A new class created when a parent class is extended. The child class inherits all of the attributes and methods of the parent class.
constructor
An optional specially named method (__init__) that is called at the moment when a class is being used to construct an object.
 Usually this is used to set up initial values for the object.
destructor
An optional specially named method (__del__) that is called at the moment just before an object is destroyed. Destructors are rarely used.
inheritance
When we create a new class (child) by extending an existing class (parent). 
The child class has all the attributes and methods of the parent class plus additional attributes and methods defined by the child class.
method
A function that is contained within a class and the objects that are constructed from the class. 
Some object-oriented patterns use ‘message’ instead of ‘method’ to describe this concept.
object
A constructed instance of a class. An object contains all of the attributes and methods that were defined by the class. 
Some object-oriented documentation uses the term ‘instance’ interchangeably with ‘object’.
parent class
The class which is being extended to create a new child class. The parent class contributes all of its methods and attributes to the new child class.

'''