


# perent class
class Organizm():
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = 'Sequance A'
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDna: {}\nOrigin: {}\nCarbon based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg


# child class inctance
class Human(Organizm):
    name = 'macQuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuiry(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

# another child class inctance
class Dog(Organizm):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Sequance B'
    origin = 'Earth'


    def bit(self):
        msg = "\nEmits a load, menacing growl and bites down ferociously on it's target!"
        return msg


# another child class inctance
class Bacterium(Organizm):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Sequance C'
    origin = 'Mars'


    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organizms!"
        return msg
    


if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuiry())

    dog = Dog()
    print(dog.information())
    print(dog.bit())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
    
