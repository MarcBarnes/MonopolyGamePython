# decent example of buttons
# https://inventwithpython.com/blog/2012/10/30/designing-a-button-ui-module-for-pygame/

import sys, pygame, random
from pygame.locals import *
from RealEstateDictionary import EstateDict
import Dice
from communityChest import communityChest
from communityChest import communityChestCard
from Chance import Chance
pygame.init()

PLAYERCOLOR = [(0,   0, 255), (0, 255,   0), (255,   0,   0), (255, 255, 0)] #BLUE, GREEN, RED, YELLOW

import random


class Dice(object):
    def __init__(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.total = 0
        self.counter = 0

    def rollDice(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.total = 0
        print("First Dice is a " + str(self.dice1))
        print("Second Dice is a " + str(self.dice2))
        self.total += self.dice1
        self.total += self.dice2
        print("Sum of both Dices is: " + str(self.total))
        self.doubleChecker()
        return self.total

    def doubleChecker(self):
        if (self.counter == 3):
            print("You rolled the same two numbers 3 times! it's time to go to Jail!")
            # gotoJail()
            self.counter = 0
            return False

        if (self.dice1 == self.dice2):
            self.counter += 1


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


class Player:
    def __init__(self, number):
        self.position = 1
        self.isPlayerBankrupt = False
        self.number = number
        self.money = 1500
        self.numProperties = 0
        if self.number == 1:
            self.pawnColor = PLAYERCOLOR[0]
        if self.number == 2:
            self.pawnColor = PLAYERCOLOR[1]
        if self.number == 3:
            self.pawnColor = PLAYERCOLOR[2]
        if self.number == 4:
            self.pawnColor = PLAYERCOLOR[3]

        self.myDice = Dice()
        self.jailCounter = 0

    def move(self):
        num = self.myDice.rollDice()
        oldPosition = self.position
        self.position = (self.position + num) % 40 + 1
        if self.position != 31:
            if self.position < oldPosition:
                self.money = self.money + 200

    def paintPosition(self):
        #random.seed()                                              #uncomment if bored or if you want to play hardmode
        #self.position = random.randint(1,40)
        if self.position == 1:
            a1 = pygame.draw.circle(screen, self.pawnColor, (700, 700 + self.number), 20, 0)
        if self.position == 2:
            a2 = pygame.draw.circle(screen, self.pawnColor, (630, 700 + self.number), 20, 0)
        if self.position == 3:
            a3 = pygame.draw.circle(screen, self.pawnColor, (565, 700 + self.number), 20, 0)
        if self.position == 4:
            a4 = pygame.draw.circle(screen, self.pawnColor, (500, 700 + self.number), 20, 0)
        if self.position == 5:
            a5 = pygame.draw.circle(screen, self.pawnColor, (440, 700 + self.number), 20, 0)
        if self.position == 6:
            a6 = pygame.draw.circle(screen, self.pawnColor, (380, 700 + self.number), 20, 0)
        if self.position == 7:
            a7 = pygame.draw.circle(screen, self.pawnColor, (315, 700 + self.number), 20, 0)
        if self.position == 8:
            a8 = pygame.draw.circle(screen, self.pawnColor, (255, 700 + self.number), 20, 0)
        if self.position == 9:
            a9 = pygame.draw.circle(screen, self.pawnColor, (190, 700 + self.number), 20, 0)
        if self.position == 10:
            a10 = pygame.draw.circle(screen, self.pawnColor, (130, 700 + self.number), 20, 0)
        if self.position == 11:
            a11 = pygame.draw.circle(screen, self.pawnColor, (60, 700 + self.number), 20, 0)
        if self.position == 12:
            a12 = pygame.draw.circle(screen, self.pawnColor, (60, 630 + self.number), 20, 0)
        if self.position == 13:
            a13 = pygame.draw.circle(screen, self.pawnColor, (60, 565 + self.number), 20, 0)
        if self.position == 14:
            a14 = pygame.draw.circle(screen, self.pawnColor, (60, 505 + self.number), 20, 0)
        if self.position == 15:
            a15 = pygame.draw.circle(screen, self.pawnColor, (60, 445 + self.number), 20, 0)
        if self.position == 16:
            a16 = pygame.draw.circle(screen, self.pawnColor, (60, 380 + self.number), 20, 0)
        if self.position == 17:
            a17 = pygame.draw.circle(screen, self.pawnColor, (60, 315 + self.number), 20, 0)
        if self.position == 18:
            a18 = pygame.draw.circle(screen, self.pawnColor, (60, 250 + self.number), 20, 0)
        if self.position == 19:
            a19 = pygame.draw.circle(screen, self.pawnColor, (60, 185 + self.number), 20, 0)
        if self.position == 20:
            a20 = pygame.draw.circle(screen, self.pawnColor, (60, 120 + self.number), 20, 0)
        if self.position == 21:
            a21 = pygame.draw.circle(screen, self.pawnColor, (60, 50 + self.number), 20, 0)
        if self.position == 22:
            a22 = pygame.draw.circle(screen, self.pawnColor, (125, 50 + self.number), 20, 0)
        if self.position == 23:
            a23 = pygame.draw.circle(screen, self.pawnColor, (190, 50 + self.number), 20, 0)
        if self.position == 24:
            a24 = pygame.draw.circle(screen, self.pawnColor, (250, 50 + self.number), 20, 0)
        if self.position == 25:
            a25 = pygame.draw.circle(screen, self.pawnColor, (310, 50 + self.number), 20, 0)
        if self.position == 26:
            a26 = pygame.draw.circle(screen, self.pawnColor, (375, 50 + self.number), 20, 0)
        if self.position == 27:
            a27 = pygame.draw.circle(screen, self.pawnColor, (440, 50 + self.number), 20, 0)
        if self.position == 28:
            a28 = pygame.draw.circle(screen, self.pawnColor, (505, 50 + self.number), 20, 0)
        if self.position == 29:
            a29 = pygame.draw.circle(screen, self.pawnColor, (570, 50 + self.number), 20, 0)
        if self.position == 30:
            a30 = pygame.draw.circle(screen, self.pawnColor, (630, 50 + self.number), 20, 0)
        if self.position == 31:
            a31 = pygame.draw.circle(screen, self.pawnColor, (700, 50 + self.number), 20, 0)
        if self.position == 32:
            a32 = pygame.draw.circle(screen, self.pawnColor, (700, 125 + self.number), 20, 0)
        if self.position == 33:
            a33 = pygame.draw.circle(screen, self.pawnColor, (700, 195 + self.number), 20, 0)
        if self.position == 34:
            a34 = pygame.draw.circle(screen, self.pawnColor, (700, 255 + self.number), 20, 0)
        if self.position == 35:
            a35 = pygame.draw.circle(screen, self.pawnColor, (700, 315 + self.number), 20, 0)
        if self.position == 36:
            a36 = pygame.draw.circle(screen, self.pawnColor, (700, 375 + self.number), 20, 0)
        if self.position == 37:
            a37 = pygame.draw.circle(screen, self.pawnColor, (700, 440 + self.number), 20, 0)
        if self.position == 38:
            a38 = pygame.draw.circle(screen, self.pawnColor, (700, 505 + self.number), 20, 0)
        if self.position == 39:
            a39 = pygame.draw.circle(screen, self.pawnColor, (700, 560 + self.number), 20, 0)
        if self.position == 40:
            a40 = pygame.draw.circle(screen, self.pawnColor, (700, 625 + self.number), 20, 0)

    def takeTurn(self, numTurns):                       # print menu for each players turn and add one to turnsTaken and work as the way for the turn to be taken
        self.takingTurn = True                               # true until turn is over
        numTurns = numTurns + 1
        updateSideBar()
        while self.takingTurn:
            pos = pygame.mouse.get_pos()
            RollDice = button(PLAYERCOLOR[0], 752*(1/4), 754, 200, 50, "Roll Dice")
            RollDice.draw(screen)
            BuyHouses = button(PLAYERCOLOR[1], 400, 754, 300, 50, "BUY HOUSES")
            BuyHouses.draw(screen)
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():  # end python interpretter if window has been closed
                if event.type == pygame.QUIT:
                    self.takingTurn = False
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:    # roll dice has been pushed
                    if RollDice.isOver(pos):
                        print("Roll Dice")
                        self.move()
                        self.checkForJail()
                        choice = self.checkCanBuy()
                        i_tax = self.checkForIncomeTax()
                        l_tax = self.checkForLuxuryTax()

                        if self.position == 3 or self.position == 8 or self.position == 18 or self.position == 23 or self.position == 34 or self.position == 37:
                            waitingToClick = True
                            currentPlayerCard = self.CheckforChanceOrChest()
                            while waitingToClick:
                                #print("Within CooC function")
                                screen.blit(bg, [0, 0])
                                prompt = button(PLAYERCOLOR[0], 100, 752 * (1 / 3), 754 - 200, 100, str(currentPlayerCard))
                                ok = button((0, 255, 0), 754 / 2 - (754 * (1 / 4)), 752 / 2, 75, 50, "Ok")
                                ok.draw(screen)
                                prompt.draw(screen)
                                pygame.display.update()
                                for event in pygame.event.get():  # end python interpretter if window has been closed
                                    pos = pygame.mouse.get_pos()
                                    if event.type == pygame.QUIT:
                                        running = False
                                        quit()

                                    if event.type == pygame.MOUSEBUTTONDOWN:  # start has been pushed
                                        if ok.isOver(pos):
                                            print("Player ", self.number, "has", self.money)
                                            waitingToClick = False

                        if choice:
                            waitingToBuy = True
                            while waitingToBuy:
                                screen.blit(bg, [0, 0])
                                prompt = button(PLAYERCOLOR[0], 100, 752 * (1 / 3), 754 -200, 100, "Buy " + EstateDict[self.position]["estateName"] + " ?")
                                yes = button((0, 255, 0), 754 / 2 - (754 * (1/4)), 752 / 2, 75, 50, "Yes")
                                no = button((255, 0, 0), 754 / 2 + (754 * (1/4)), 752 / 2, 75, 50, "No")
                                prompt.draw(screen)
                                yes.draw(screen)
                                no.draw(screen)
                                pygame.display.update()
                                for event in pygame.event.get():  # end python interpretter if window has been closed
                                    pos = pygame.mouse.get_pos()
                                    if event.type == pygame.QUIT:
                                        running = False
                                        quit()

                                    if event.type == pygame.MOUSEBUTTONDOWN:  # start has been pushed
                                        if yes.isOver(pos):
                                            EstateDict[self.position]["ownerNumber"] = self.number
                                            self.money = self.money - int(EstateDict[self.position]["price"])
                                            print("Player ", self.number, "has", self.money)
                                            self.numProperties = self.numProperties + 1
                                            waitingToBuy = False

                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if no.isOver(pos):
                                            waitingToBuy = False

                        if i_tax:
                            waitingToPay = True
                            while waitingToPay:
                                screen.blit(bg, [0, 0])
                                prompt = button(PLAYERCOLOR[0], 100, 752 * (1 / 3), 754 -200, 100, "Pay Income Tax")
                                buttonPay200 = button((0, 255, 0), 754 / 2 - (754 * (1/4)), 752 / 2, 75, 50, "$200")
                                buttonPay10P = button((255, 0, 0), 754 / 2 + (754 * (1/4)), 752 / 2, 75, 50, "10%")
                                prompt.draw(screen)
                                buttonPay200.draw(screen)
                                buttonPay10P.draw(screen)
                                pygame.display.update()
                                for event in pygame.event.get():  # end python interpretter if window has been closed
                                    pos = pygame.mouse.get_pos()
                                    if event.type == pygame.QUIT:
                                        running = False
                                        quit()

                                    if event.type == pygame.MOUSEBUTTONDOWN:  # start has been pushed
                                        if buttonPay200.isOver(pos):
                                            self.money = self.money - 200
                                            print("Player ", self.number, "has", self.money, "Player paid $200")
                                            waitingToPay = False

                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if buttonPay10P.isOver(pos):
                                            self.money = self.money - .1*self.money
                                            print("Player ", self.number, "has", self.money,"Player paid 10% of current money")
                                            waitingToPay = False
                        if l_tax:
                            waitingToPayLux = True
                            while waitingToPayLux:
                                screen.blit(bg, [0, 0])
                                prompt = button(PLAYERCOLOR[0], 100, 752 * (1 / 3), 754 -200, 100, "Pay Luxury Tax")
                                pay75 = button((0, 255, 0), 754 / 2 - (754 * (1 / 4)), 752 / 2, 75, 50, "$75")
                                prompt.draw(screen)
                                pay75.draw(screen)
                                pygame.display.update()
                                for event in pygame.event.get():  # end python interpretter if window has been closed
                                    pos = pygame.mouse.get_pos()
                                    if event.type == pygame.QUIT:
                                        running = False
                                        quit()

                                    if event.type == pygame.MOUSEBUTTONDOWN:  # start has been pushed
                                        if pay75.isOver(pos):
                                            self.money = self.money - 75
                                            print("Player ", self.number, "has", self.money, "Player paid $75")
                                            waitingToPayLux = False


                        self.takingTurn = False

                if event.type == pygame.MOUSEBUTTONDOWN:    # buy houses has been pushed
                    if BuyHouses.isOver(pos):
                        print("Buying Houses")
                        self.buyAHouse()

            for p in players:
                p.paintPosition()
            pygame.display.update()

        return numTurns

    def buyAHouse(self):
        jayarama = True
        while jayarama and self.numProperties != 0:
            pos = pygame.mouse.get_pos()
            print("jayarama")
            for property in sideBar:
                print("property")
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and property.isOver(pos):
                        tempButton = property
                        propertyIndex = 0
                        for estate in EstateDict:
                            print(estate)
                            if EstateDict[estate]["estateName"] == property.text.split(':')[0]:
                                print(tempButton.text)
                                propertyIndex = estate
                        if int(EstateDict[propertyIndex]["houses"]) > 3:
                            jayarama = False
                            break

                        if players[theBoard.totalTurnsTaken % theBoard.numPlayers].money >= int(EstateDict[estate]["houseCost"]):
                            print(propertyIndex)
                            jayarama = False
                            EstateDict[propertyIndex]["houses"] = str(int(EstateDict[propertyIndex]["houses"]) + 1)
                            players[theBoard.totalTurnsTaken % theBoard.numPlayers].money = players[theBoard.totalTurnsTaken % theBoard.numPlayers].money - int(EstateDict[propertyIndex]["houseCost"])
                            print("you bought", EstateDict[propertyIndex]["estateName"])

                    property.draw(screen)
                    pygame.display.update()

    def CheckforChanceOrChest(self):
        playerslist = players

        for p in playerslist:
            print("INITIAL POSITION", p.position)


        # Community Chest
        if (self.position == 3 or self.position == 18 or self.position == 34):
            test = str(self.position)
            print("Position chest", test)
            chest = communityChest()
            currentPlayerCard = chest.selectCardforCurrentPlayer()

            if (currentPlayerCard.type == 'go To'):
                if self.position > currentPlayerCard.effect:
                    self.money = self.money + 200
                self.position = currentPlayerCard.effect
            elif (currentPlayerCard.type == 'Advance to GO'):
                self.position = currentPlayerCard.effect
            elif (currentPlayerCard.type == 'cash'):
                self.money = self.money + currentPlayerCard.effect
            elif (currentPlayerCard.type == 'give'):

                j = 0

                while(j != len(playerslist)-1):
                    self.money = self.money - 10
                    j += 1

                i = 0

                while (i != len(playerslist)):
                    if (playerslist[i].number != self.number):
                        playerslist[i].money = playerslist[i].money + 10
                        i += 1
                    else:
                        i += 1
                        continue

            elif (currentPlayerCard.type == 'receive'):

                j = 0

                while (j != len(playerslist)-1):
                    self.money = self.money + 10
                    j += 1

                i = 0

                while (i != len(playerslist)):
                    if (playerslist[i].number != self.number):
                        playerslist[i].money = playerslist[i].money - 10
                        i += 1
                    else:
                        i += 1
                        continue

            for p in playerslist:
                print("NEW POSITION", p.position)

            print(currentPlayerCard.type, "within Comutitty chest", self.money)
            pygame.display.update()
            return currentPlayerCard

        # Chance
        if (self.position == 8 or self.position == 23 or self.position == 37):
            test = str(self.position)
            print("Position chest", test)
            chance = Chance()
            currentPlayerCard = chance.selectCardforCurrentPlayer()

            if (currentPlayerCard.type == 'go To'):
                if self.position > currentPlayerCard.effect:
                    self.money = self.money + 200
                self.position = currentPlayerCard.effect
            elif (currentPlayerCard.type == 'Advance to GO'):
                self.position = currentPlayerCard.effect
            elif (currentPlayerCard.type == 'Go to Jail'):
                self.position = currentPlayerCard.effect
            elif (currentPlayerCard.type == 'Go To Free Parking'):
                if self.position > currentPlayerCard.effect:
                    self.money = self.money + 200
                self.position = currentPlayerCard.effect
            elif (currentPlayerCard.type == 'Go To RailRoads'):
                if self.position > currentPlayerCard.effect:
                    self.money = self.money + 200
                self.position = currentPlayerCard.effect
            elif (currentPlayerCard.type == 'cash'):
                self.money = self.money + currentPlayerCard.effect
            elif (currentPlayerCard.type == 'give'):

                j = 0

                while (j != len(playerslist)-1):
                    self.money = self.money - 10
                    j += 1

                i = 0

                while (i != len(playerslist)):
                    if (playerslist[i].number != self.number):
                        playerslist[i].money = playerslist[i].money + 10
                        i += 1
                    else:
                        i += 1
                        continue

            elif (currentPlayerCard.type == 'receive'):
                j = 0

                while (j != len(playerslist)-1):
                    self.money = self.money + 10
                    j += 1

                i = 0

                while (i != len(playerslist)):
                    if (playerslist[i].number != self.number):
                        playerslist[i].money = playerslist[i].money + 10
                        i += 1
                    else:
                        i += 1
                        continue
            print(currentPlayerCard.type, "within Chance", self.money)
            pygame.display.update()

            for p in playerslist:
                print("NEW POSITION", p.position)

            return currentPlayerCard

    def checkForIncomeTax(self):

        if self.position == 5:
            return True
        return False

    def checkForLuxuryTax(self):

        if self.position == 39:
            return True
        return False

    def checkCanBuy(self):
        for i in EstateDict:
            if self.position == i:
                if int(EstateDict[i]["ownerNumber"]) == -1:
                    if self.money >= int(EstateDict[i]["price"]):
                        return True
                    else:
                        return False

                else:
                    self.payRent()
                    return False

    def checkForJail(self):
        if(self.jailCounter > 1 and self.jailCounter < 4):

            if self.jailCounter == 2:
                print(self.jailCounter)
                self.position = 11
                self.jailCounter = 3

            elif self.jailCounter == 3:
                print(self.jailCounter)
                self.jailCounter = 0
                self.position = 12

        if (self.position == 31):
            print("PLAYER IS GOING TO JAIL")

            self.jailCounter = 1

            self.position = 11

        if (self.jailCounter == 1 and self.position == 11):

            self.position = 11
            self.jailCounter = 2

    def buyHouse(self):
        if EstateDict[self.position]['houses'] < 4 and EstateDict[self.position]['monopoly']:
            self.money = self.money - EstateDict[self.position]['houseCost']
            return True
        else:
            return False

    def payRent(self):
        self.playerHasPaid = False
        while self.playerHasPaid == False:
            if self.isPlayerBankrupt:
                return False
            elif self.number == int(EstateDict[self.position]['ownerNumber']):  # they own it
                return True ####insert
            elif int(EstateDict[self.position]['rent']) <= self.money and int(EstateDict[self.position]['monopoly']) == 0:  # they don't own it but they have the money to pay for it and no monopoly
                numHOUSES = EstateDict[self.position]['houses']
                playerToPay = EstateDict[self.position]['ownerNumber']
                if numHOUSES == 0:
                    self.money = self.money - EstateDict[self.position]['rent']
                    players[playerToPay].money = players[playerToPay].money + EstateDict[self.position]['rent']

                elif numHOUSES == 1:
                    self.money = self.money - EstateDict[self.position]['own']
                    players[playerToPay].money = players[playerToPay].money + EstateDict[self.position]['own1HouseRent']

                elif numHOUSES == 2:
                    self.money = self.money - EstateDict[self.position]['rent']
                    players[playerToPay].money = players[playerToPay].money + EstateDict[self.position]['own2HouseRent']

                elif numHOUSES == 3:
                    self.money = self.money - EstateDict[self.position]['rent']
                    players[playerToPay].money = players[playerToPay].money + EstateDict[self.position]['own3HouseRent']

                elif numHOUSES == 4:
                    self.money = self.money - EstateDict[self.position]['rent']
                    players[playerToPay].money = players[playerToPay].money + EstateDict[self.position]['own4HouseRent']

###end insert
                return True
            elif EstateDict[self.position]['monopoly'] == 1:
                if self.money >= EstateDict[self.position]['price'] * 2:
                    self.money = self.money - (EstateDict[self.position]['price'] * 2)
                    return True
                else:
                    self.mortgageProperty()
            elif EstateDict[self.position]['rent'] > self.money:  # if they don't have the money, mortgage off properties
                self.mortgageProperty()

    def mortgageProperty(self):
        for property in EstateDict:
            if property['ownerNumber'] == self.number:
                if property['hotel'] > 0:  # mortgages hotel
                    self.money = self.money + property['houseValue']
                    property['hotel'] = 0
                    self.payRent()
                elif property['houses'] > 0:  # mortgages houses
                    self.money = self.money + property['houseValule']
                    property['houses'] = property['houses'] - 1
                    self.payRent()
                elif property['mortgaged'] == 0:  # mortgages property itself
                    self.money = self.money + property['mortgageValue']
                    property['mortgaged'] = 1
                    self.payRent()
        self.isPlayerBankrupt = True  # if we exit for

    def buyProperty(self):
        if EstateDict[self.position]['available'] == 1 and self.money >= EstateDict[self.position]['price']:
            self.money = self.money - EstateDict[self.position]['price']
            EstateDict[self.position]['ownerNumber'] = self.number
            return True
        else:
            return False

    def isPropertyOwner(self):
        if EstateDict[self.position]['ownerNumber'] == self.number:
            return True
        return False

    # def buyProperty(self):
    #     if EstateDict[self.position]['available'] == 1:
    #         if self.money < EstateDict[self.position]['price']:
    #             return False
    #         else:
    #             self.money = self.money - EstateDict[self.position]['price']
    #             if self.checkForMonopoly(EstateDict[self.position]['group']):
    #                 for element in EstateDict:
    #                     if element['group'] == EstateDict[self.position]['group'] and element['ownerNumber'] == self.number:
    #                         element['monopoly'] = 1
    #             EstateDict[self.position]['ownerNumber'] = self.number
    #             return True

    def checkForMonopoly(self, color):
        self.monopoly = True
        for element in EstateDict:
            if element['group'] == color and element['ownerNumber'] != self.number:
                self.monopoly = False
        return self.monopoly

class Board:
    def __init__(self):
        self.numPlayers = 0
        self.totalTurnsTaken = 0
        self.gameHasStarted = False
        self.numPlayersChosen = False
        self.setupBoard()
        b = button((255, 255, 255), 750 / 2 - 375, 754, 750, 50, "")
        b.draw(screen)
        pygame.display.update()

    def setupBoard(self):
        running = True
        while running:
            screen.blit(bg, [0, 0])  # paint the backgorund image in the back first so it doesnt cover anything
            startButton = button((0,255,255),752/2 -50, 754, 125, 50, "Start?")
            print("Painting Background")  # debug comment
            for event in pygame.event.get():  # end python interpretter if window has been closed
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    running = False
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:  # start has been pushed
                    if startButton.isOver(pos):
                        self.gameHasStarted = True
                        print("Game has started")

            if self.gameHasStarted == False:
                print("Drawing start button")
                startButton.draw(screen)

            if self.gameHasStarted:
                if self.numPlayersChosen == False:
                    print("Drawing howManyPlayers text")
                    pressedKey = pygame.key.get_pressed()
                    self.howManyPlayers = button((0, 255, 255), 750 / 2 - 375, 754, 750, 50, "How many Players?(2-4)")
                    self.howManyPlayers.draw(screen)
                    if pressedKey[K_2]:
                        self.numPlayers = 2
                        self.numPlayersChosen = True

                    if pressedKey[K_3]:
                        self.numPlayers = 3
                        self.numPlayersChosen = True

                    if pressedKey[K_4]:
                        self.numPlayers = 4
                        self.numPlayersChosen = True

                if self.numPlayersChosen:
                    running = False

            pygame.display.flip()
            pygame.display.update()


def updateSideBar():
    white = (255,255,255)
    pixelcount = 0
    whiteOutButton = button(white, 752 , pixelcount, 448, 800, "")
    whiteOutButton.draw(screen)
    pixelcount = pixelcount + 40
    currentPlayer = button(white, 752 , pixelcount, 448, 15, "Player " + str(players[(theBoard.totalTurnsTaken % theBoard.numPlayers)].number) + "\'s turn")
    currentPlayer.draw(screen)
    pixelcount = pixelcount + 40
    currentBank = button(white, 752 , pixelcount, 448, 15, "Money: " + str(players[(theBoard.totalTurnsTaken % theBoard.numPlayers)].money))
    currentBank.draw(screen)
    pixelcount = pixelcount + 40
    sideBar.clear()
    for estate in EstateDict:
        if int(EstateDict[estate]["ownerNumber"]) == (players[(theBoard.totalTurnsTaken % theBoard.numPlayers)].number):
            e = button(white, 752, pixelcount, 448, 15, EstateDict[estate]["estateName"] + ": " + EstateDict[estate]["houses"])
            e.draw(screen)
            sideBar.append(e)
            pixelcount = pixelcount + 40

def checkForWin():
    for p in players:
        if p.money <= 0:
            players.remove(p)
            for p2 in players:
                max = p2.money




if __name__ == "__main__":
    bg = pygame.image.load("monopoly.jpg")
    width, height = 1200, 800                                        # set size of the window. The size of the image is 752,754 but I went to 800 to add space for buttons
    screen = pygame.display.set_mode((width, height))
    theBoard = Board()
    gameHasNotBeenWon = True
    players = []
    i = 1
    sideBar = []
    while(i <= theBoard.numPlayers):
        p = Player(i)
        players.append(p)
        print("player" , i , "has been created")
        i = i + 1

    while(gameHasNotBeenWon):
        screen.blit(bg, [0, 0])
        theBoard.totalTurnsTaken = players[(theBoard.totalTurnsTaken % theBoard.numPlayers)].takeTurn(theBoard.totalTurnsTaken)
        print("Number of turns taken: ", theBoard.totalTurnsTaken)
        for p in players:
            p.paintPosition()

        pygame.display.update()
