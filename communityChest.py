import random

class communityChestCard:
    
    #type - are you moving player position or affecting bank account
    #effect - by how much
    
    def __init__(self,type,effect):
        
        self.type = type
        self.effect = effect

    def __str__(self):
        
        return "Community Card (%s,%s)" % (self.type,self.effect)

#communityChest considered to be "Money Deck" so more money cards
class communityChest:
    
    CASH = [10,20,30,40,50,60,70,80,90,100,150,200,-10,-20,-30,-40,-50,-60,-70,-80,-90,-100,-150,-200]
    
    CARDS = [communityChestCard('go To', random.randint(2,40)),
             communityChestCard('Advance to GO', 1),
             communityChestCard('cash',random.choice(CASH)),
             communityChestCard('cash',random.choice(CASH)),
             communityChestCard('cash',random.choice(CASH)),
             communityChestCard('cash',random.choice(CASH)),
             communityChestCard('give', 10), #to every other player
             communityChestCard('receive', 10), #to every other player
             communityChestCard('cash',random.choice(CASH)),
             communityChestCard('give', 10), #to every other player
             communityChestCard('receive', 10) #to every other player
            ]

    def __init__(self):
    
        random.shuffle(self.CARDS)
    

    def selectCardforCurrentPlayer(self):

        currentPlayersCard = self.CARDS[0]

        random.shuffle(self.CARDS)

        return currentPlayersCard

#tester
if __name__ == "__main__":

    x = communityChest()

    playerCard = x.selectCardforCurrentPlayer()

    print(playerCard)






