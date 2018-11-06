import random

class Dice(object):
    
    def __init__(self):
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        self.total = 0
        self.counter = 0
        
    def rollDice(self):

        print("First Dice is a " + str(self.dice1))
        print("Second Dice is a " + str(self.dice2))
        
        self.total += self.dice1
        
        self.total += self.dice2
    
        print("Sum of both Dices is: " + str(self.total))
    
        self.doubleChecker(self.total)
    
    
    def doubleChecker(self,temp):
        
        if(self.counter == 3):
            
            print("You rolled the same two numbers 3 times! it's time to go to Jail!")
            #gotoJail()
            
            return False
        
        if(self.dice1 == self.dice2):

            self.counter += 1
            
            self.total = temp
            
            self.rollDice()

            return True


#Testing to see if works

if __name__ == "__main__":

    player1 = Dice()

    player1.rollDice()








