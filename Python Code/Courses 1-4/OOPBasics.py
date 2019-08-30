#This creates a template for "Party Animals"
#Each PartyAnimal object has a bit of data x=0
#Each PartyAnimal object also has a bit of code. We can apply the party function
#to manipulate the PartyAnimal data in that particular object


class PartyAnimal:
    x=0

#prints when object is created
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

#prints when object is destroyed
    def __del__(self):
        print ('I am destructed', self.x)

#This is used to CONSTUCT a basic PartyAnimal named "an"
an = PartyAnimal()

an.party()
an.party()
an = 42
print ('an contains', an)
