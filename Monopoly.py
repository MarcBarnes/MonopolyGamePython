# decent example of buttons
# https://inventwithpython.com/blog/2012/10/30/designing-a-button-ui-module-for-pygame/

import sys, pygame, random
from pygame.locals import *
from RealEstateDictionary import EstateDict
import Dice
import communityChest
import Chance
pygame.init()

PLAYERCOLOR = [(0,   0, 255), (0, 255,   0), (255,   0,   0), (255, 255, 0)] #BLUE, GREEN, RED, YELLOW
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
        self.number = number
        if self.number == 1:
            self.pawnColor = PLAYERCOLOR[0]
        if self.number == 2:
            self.pawnColor = PLAYERCOLOR[1]
        if self.number == 3:
            self.pawnColor = PLAYERCOLOR[2]
        if self.number == 4:
            self.pawnColor = PLAYERCOLOR[3]

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
        numTurns = numTurns + 1                         #
        while self.takingTurn:
            for event in pygame.event.get():  # end python interpretter if window has been closed
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.takingTurn = False
                    quit()

                pos = pygame.mouse.get_pos()
                RollDice = button(PLAYERCOLOR[0], 100, 754, 150, 50, str(numTurns % 4) + " Rolling")
                RollDice.draw(screen)
                BuyHouses = button(PLAYERCOLOR[1], 400, 754, 300, 50, "BUY HOUSES")
                BuyHouses.draw(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:    # roll dice has been pushed
                    if RollDice.isOver(pos):
                        print("Roll Dice")
                        self.takingTurn = False

                if event.type == pygame.MOUSEBUTTONDOWN:    # buy houses has been pushed
                    if BuyHouses.isOver(pos):
                        print("Buying Houses")
                        self.takingTurn = False

            return numTurns

    def buyHotel(self, name):
        if EstateDict[name]['houses'] == 4:
            self.money = self.money = EstateDict[name]['houseCost']
            return True
        else:
            return False

    def buyHouse(self, name):
        if EstateDict[name]['houses'] < 4 and EstateDict[name]['monopoly']:
            self.money = self.money - EstateDict[name]['houseCost']
            return True
        else:
            return False

    def isPlayerBankrupt(self):
        return self.isPlayerBankrupt

    def payRent(self, name):
        self.playerHasPaid = False
        while self.playerHasPaid == False:
            if self.isPlayerBankrupt:
                return False
            elif self.number == EstateDict[name]['ownerNumber']:  # they own it
                return True
            elif EstateDict[name]['rent'] <= self.money:  # they don't own it but they have the money to pay for it
                self.money = self.money - EstateDict[name]['rent']
                return True
            elif EstateDict[name]['rent'] > self.money:  # if they don't have the money, mortgage off properties
                self.mortgageProperty(name)

    def mortgageProperty(self, name):
        for property in EstateDict:
            if property['ownerNumber'] == self.number:
                if property['hotel'] > 0:  # mortgages hotel
                    self.money = self.money + property['houseValue']
                    property['hotel'] = 0
                    self.payRent(name)
                elif property['houses'] > 0:  # mortgages houses
                    self.money = self.money + property['houseValule']
                    property['houses'] = property['houses'] - 1
                    self.payRent(name)
                elif property['mortgaged'] == 0:  # mortgages property itself
                    self.money = self.money + property['mortgageValue']
                    property['mortgaged'] = 1
                    self.payRent(name)
        self.isPlayerBankrupt = True  # if we exit for

    def getMoney(self):
        return self.money

    def buyProperty(self, name):
        if EstateDict[name]['available'] == 1 and self.money >= EstateDict[name]['price']:
            self.money = self.money - EstateDict[name]['price']
            EstateDict[name]['ownerNumber'] = self.number
            return True
        else:
            return False

    def isPropertyOwner(self, name):
        if EstateDict[name]['ownerNumber'] == self.number:
            return True
        return False

class Board:
    def __init__(self):
        self.numPlayers = 0
        self.totalTurnsTaken = 0
        self.gameHasStarted = False
        self.numPlayersChosen = False
        self.setupBoard()

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


if __name__ == "__main__":
    bg = pygame.image.load("monopoly.jpg")
    width, height = 752, 800                                        # set size of the window. The size of the image is 752,754 but I went to 800 to add space for buttons
    screen = pygame.display.set_mode((width, height))
    theBoard = Board()
    gameHasNotBeenWon = True
    players = []
    i = 1
    while(i <= theBoard.numPlayers):
        p = Player(i)
        players.append(p)
        print("player" , i , "has been created")
        i = i + 1

    while(gameHasNotBeenWon):
        screen.blit(bg, [0, 0])
        theBoard.totalTurnsTaken = players[(theBoard.totalTurnsTaken % theBoard.numPlayers)].takeTurn(theBoard.totalTurnsTaken)
        for p in players:
            p.paintPosition()

        pygame.display.update()

