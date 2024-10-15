#This concept has been hard for me to grasp
#So to understand it, I have created a framework,
#The framework is CLFA
#clfa is an abbreviation for Concept-Logic-Function-Application

stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))

''' 
Instead of focusing on what these lines accomplish, let’s look at what is really happening from the point of view of object-oriented programming. 
Don’t worry if the following paragraphs don’t make any sense the first time you read them because we have not yet defined all of these terms.
The first line constructs an object of type list, the second and third lines call the append() method, the fourth line calls the sort() method,
and the fifth line retrieves the item at position 0.
The sixth line calls the __getitem__() method in the stuff list with a parameter of zero.
The seventh line calls the __getitem__() method in the list class with the stuff list and a parameter of zero.
The eighth line is a comment and does not do anything when the program runs.

'''

class PartyAnimal:

   def __init__(self):
     self.x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far",self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()

class PartyAnimal:

   def __init__(self):
     self.x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far",self.x)

an = PartyAnimal()
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))

class PartyAnimal:

   def __init__(self):
     self.x = 0
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):
     print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)

class PartyAnimal:

   def __init__(self, nam):
     self.x = 0
     self.name = nam
     print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)

s = PartyAnimal('Sally')
s.party()
j = PartyAnimal('Jim')

j.party()
s.party()