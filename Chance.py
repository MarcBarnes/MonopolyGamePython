import random

class chanceCard:
    
    #type - are you moving player position or affecting bank account
    #effect - by how much
    
    def __init__(self,type,effect):
        
        self.type = type
        self.effect = effect
    
    def __str__(self):
        
        return "Chance Card (%s,%s)" % (self.type,self.effect)


#Chance is considered to be "Movement Deck" so more movement cards
class Chance:

    random.seed()
    
    RAILROADS = [6,16,26,36]
    
    UTILTIES = [13,29]
    
    CASH = [10,20,30,40,50,60,70,80,90,100,150,200,-10,-20,-30,-40,-50,-60,-70,-80,-90,-100,-150,-200]
    
    CARDS = [chanceCard('go To', random.randint(2,40)),
             chanceCard('go To', random.randint(2,40)),
             chanceCard('go To', random.randint(2,40)),
             chanceCard('go To', random.randint(2,40)),
             chanceCard('Advance to GO', 1),
             chanceCard('Go To Jail', 31),
             chanceCard('Go To Free Parking', 21),
             chanceCard('Go To RailRoads', random.choice(RAILROADS)),
             chanceCard('Go to BoardWalk', 40),
             chanceCard('cash',random.choice(CASH)),
             chanceCard('give', 10), #to every other player
             chanceCard('receive', 10) #to every other player
             ]
        
    def __init__(self):
                 
        random.shuffle(self.CARDS)


    def selectCardforCurrentPlayer(self):
    
        currentPlayersCard = self.CARDS[0]
        
        random.shuffle(self.CARDS)

        print(currentPlayersCard)
        
        return currentPlayersCard

# #tester
# if __name__ == "__main__":
#
#     x = Chance()
#
#     playerCard = x.selectCardforCurrentPlayer()
#
#     print(playerCard)
#





