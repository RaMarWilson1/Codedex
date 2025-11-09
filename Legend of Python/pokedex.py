class Pokemon:
    def __init__(self, entry, name, types, description,is_caught):
        self.entry = entry 
        self.name = name
        self.types = types 
        self.description = description
        self.is_caught = is_caught
    
    def speak(self):
        print(self.name + " " + self.name )

    def display_details(self):
        print("Entry Number: " + str(self.entry))
        print("\n Name: " + self.name)
        print("\n Types: " + str(self.types))
        print("\nDescription: " + self.description)
        print()
        if self.is_caught == True:
            print(self.name + " has already been caught" )
        else:
            print(self.name + " has not been caught" )
        print()

Picachu = Pokemon(25,"Picachu",["Electric","stealth"],"lorem ispum", True)

Picachu.speak()
Picachu.display_details()

Speedy = Pokemon(5,"Speedy",["wind","speed"],"lorem ispum", False)

Speedy.speak()
Speedy.display_details()

kokokke = Pokemon(25,"kokokke",["Rock","Strength"],"lorem ispum", True)

kokokke.speak()
kokokke.display_details()
