class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print (self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()

# s and j are two independant instances
# ends with
# s -> x = 2
#      name = Sally
# j -> x = 1
#      name = Jim
-------------------------------------------------------------------------
#FootballFan is a class which extends PartyAnimal. It has all the
#capabilities of PartyAnimal and more.
class FootballFan (PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

st = PartyAnimal("Steph")
st.party()

Je = FootballFan("Jeff")
je.party()
je.touchdown()

# st and je are two independant instances
# st -> x = 1
#       name = Steph
# je -> x = 1
#       points = 7
#       name = Jeff
