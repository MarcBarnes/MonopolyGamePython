class Railroad(object):

    def __init__(self, name, ownedBy):
        self.price = 250
        self.name = name
        self.ownedBy = ownedBy

    def getRent(self, numberOwned):
        if numberOwned == 1:
            return 25
        elif numberOwned == 2:
            return 50
        elif numberOwned == 3:
            return 100
        elif numberOwned == 4:
            return 200

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

    def getOwner(self):
        return self.ownedBy
