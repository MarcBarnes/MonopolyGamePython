class Utility(object):

    def __init__(self, name, ownedBy):
        self.name = name
        self.ownedBy = ownedBy
        self.price = 150

    def getRent(self, diceRoll, numberOwned):
        if numberOwned < 2:
            return diceRoll * 4
        else:
            return diceRoll * 10

    def getName(self):
        return self.name

    def getOwner(self):
        return self.ownedBy

    def getPrice(self):
        return self.price
