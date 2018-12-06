import sys, pygame, random
from RealEstateDictionary import EstateDict
pygame.init()

BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
YELLOW = (255, 255, 0)

random.seed()
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

# create moveTo func

    def __init__(self, number):
        self.position = random.randint(1,40)
        self.number = number
        self.isPlayerBankrupt = False
        self.money = 1500

        if self.number == 1:
            self.pawnColor = BLUE
        elif self.number == 2:
            self.pawnColor = GREEN
        elif self.number == 3:
            self.pawnColor = RED
        elif self.number == 4:
            self.pawnColor = YELLOW

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
        else
            return False

    def isPlayerBankrupt(self):
        return self.isPlayerBankrupt

    def payRent(self, name):
        if self.isPlayerBankrupt == True:
            return False
        self.playerHasPaid = False
        while self.playerHasPaid == False:
            if self.number == EstateDict[name]['ownerNumber']:     # they own it
                return True
        elif EstateDict[name]['rent'] <= self.money:           # they don't own it but they have the money to pay for it
            self.money = self.money - EstateDict[name]['rent']
        elif EstateDict[name]['rent'] > self.money:             # if they don't have the money, mortgage off properties
            self.mortgageProperty(name)
# revisit the logic on this, bc we have a func calling a func, when we get to mortgageProp calling payRent, will it return to where it was w/i mortgageProp?
    def mortgageProperty(self, name):
        for property in EstateDict:
            if property['ownerNumber'] == self.number:
                if property['hotel'] > 0:                       # mortgages hotel
                    self.money = self.money + property['houseValue']
                    property['hotel'] = 0
                    self.payRent(name)
                elif property['houses'] > 0:                    # mortgages houses
                    self.money = self.money + property['houseValule']
                    property['houses'] = property['houses'] - 1
                    self.payRent(name)
                elif property['mortgaged'] == 0:                # mortgages property itself
                    self.money = self.money + property['mortgageValue']
                    property['mortgaged'] = 1
                    self.payRent(name)
        self.isPlayerBankrupt = True                            # if we exit for


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





if __name__ == "__main__":
    playerOne = Player(1)
    playerTwo = Player(2)
    playerThree = Player(3)
    playerFour = Player(4)

    width, height = 752, 754
    screen = pygame.display.set_mode((width, height))

    bg = pygame.image.load("monopoly.jpg")

    running = True
    while running:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:    #start has been pushed
                if startButton.isOver(pos):
                    print("Game has started")

        pygame.display.update()

        screen.blit(bg, [0,0])
        pygame.display.flip()

        def position(p):
            if p.position == 1:
                a1 = pygame.draw.circle(screen, p.pawnColor, (700, 700), 20, 0)
            if p.position == 2:
                a2 = pygame.draw.circle(screen, p.pawnColor, (630, 700), 20, 0)
            if p.position == 3:
                a3 = pygame.draw.circle(screen, p.pawnColor, (565, 700), 20, 0)
            if p.position == 4:
                a4 = pygame.draw.circle(screen, p.pawnColor, (500, 700), 20, 0)
            if p.position == 5:
                a5 = pygame.draw.circle(screen, p.pawnColor, (440, 700), 20, 0)
            if p.position == 6:
                a6 = pygame.draw.circle(screen, p.pawnColor, (380, 700), 20, 0)
            if p.position == 7:
                a7 = pygame.draw.circle(screen, p.pawnColor, (315, 700), 20, 0)
            if p.position == 8:
                a8 = pygame.draw.circle(screen, p.pawnColor, (255, 700), 20, 0)
            if p.position == 9:
                a9 = pygame.draw.circle(screen, p.pawnColor, (190, 700), 20, 0)
            if p.position == 10:
                a10 = pygame.draw.circle(screen, p.pawnColor, (130, 700), 20, 0)
            if p.position == 11:
                a11 = pygame.draw.circle(screen, p.pawnColor, (60, 700), 20, 0)
            if p.position == 12:
                a12 = pygame.draw.circle(screen, p.pawnColor, (60, 630), 20, 0)
            if p.position == 13:
                a13 = pygame.draw.circle(screen, p.pawnColor, (60, 565), 20, 0)
            if p.position == 14:
                a14 = pygame.draw.circle(screen, p.pawnColor, (60, 505), 20, 0)
            if p.position == 15:
                a15 = pygame.draw.circle(screen, p.pawnColor, (60, 445), 20, 0)
            if p.position == 16:
                a16 = pygame.draw.circle(screen, p.pawnColor, (60, 380), 20, 0)
            if p.position == 17:
                a17 = pygame.draw.circle(screen, p.pawnColor, (60, 315), 20, 0)
            if p.position == 18:
                a18 = pygame.draw.circle(screen, p.pawnColor, (60, 250), 20, 0)
            if p.position == 19:
                a19 = pygame.draw.circle(screen, p.pawnColor, (60, 185), 20, 0)
            if p.position == 20:
                a20 = pygame.draw.circle(screen, p.pawnColor, (60, 120), 20, 0)
            if p.position == 21:
                a21 = pygame.draw.circle(screen, p.pawnColor, (60, 50), 20, 0)
            if p.position == 22:
                a22 = pygame.draw.circle(screen, p.pawnColor, (125, 50), 20, 0)
            if p.position == 23:
                a23 = pygame.draw.circle(screen, p.pawnColor, (190, 50), 20, 0)
            if p.position == 24:
                a24 = pygame.draw.circle(screen, p.pawnColor, (250, 50), 20, 0)
            if p.position == 25:
                a25 = pygame.draw.circle(screen, p.pawnColor, (310, 50), 20, 0)
            if p.position == 26:
                a26 = pygame.draw.circle(screen, p.pawnColor, (375, 50), 20, 0)
            if p.position == 27:
                a27 = pygame.draw.circle(screen, p.pawnColor, (440, 50), 20, 0)
            if p.position == 28:
                a28 = pygame.draw.circle(screen, p.pawnColor, (505, 50), 20, 0)
            if p.position == 29:
                a29 = pygame.draw.circle(screen, p.pawnColor, (570, 50), 20, 0)
            if p.position == 30:
                a30 = pygame.draw.circle(screen, p.pawnColor, (630, 50), 20, 0)
            if p.position == 31:
                a31 = pygame.draw.circle(screen, p.pawnColor, (700, 50), 20, 0)
            if p.position == 32:
                a32 = pygame.draw.circle(screen, p.pawnColor, (700, 125), 20, 0)
            if p.position == 33:
                a33 = pygame.draw.circle(screen, p.pawnColor, (700, 195), 20, 0)
            if p.position == 34:
                a34 = pygame.draw.circle(screen, p.pawnColor, (700, 255), 20, 0)
            if p.position == 35:
                a35 = pygame.draw.circle(screen, p.pawnColor, (700, 315), 20, 0)
            if p.position == 36:
                a36 = pygame.draw.circle(screen, p.pawnColor, (700, 375), 20, 0)
            if p.position == 37:
                a37 = pygame.draw.circle(screen, p.pawnColor, (700, 440), 20, 0)
            if p.position == 38:
                a38 = pygame.draw.circle(screen, p.pawnColor, (700, 505), 20, 0)
            if p.position == 39:
                a39 = pygame.draw.circle(screen, p.pawnColor, (700, 560), 20, 0)
            if p.position == 40:
                a40 = pygame.draw.circle(screen, p.pawnColor, (700, 625), 20, 0)


        position(playerOne)
        position(playerTwo)
        position(playerThree)
        position(playerFour)

        # a1 = pygame.draw.circle(screen, (255,0,0), (700, 700), 20, 0)
        # a2 = pygame.draw.circle(screen, (255, 0, 0), (630, 700), 20, 0)
        # a3 = pygame.draw.circle(screen, (255, 0, 0), (565, 700), 20, 0)
        # a4 = pygame.draw.circle(screen, (255, 0, 0), (500, 700), 20, 0)
        # a5 = pygame.draw.circle(screen, (255, 0, 0), (440, 700), 20, 0)
        # a6 = pygame.draw.circle(screen, (255, 0, 0), (380, 700), 20, 0)
        # a7 = pygame.draw.circle(screen, (255, 0, 0), (315, 700), 20, 0)
        # a8 = pygame.draw.circle(screen, (255, 0, 0), (255, 700), 20, 0)
        # a9 = pygame.draw.circle(screen, (255, 0, 0), (190, 700), 20, 0)
        # a10 = pygame.draw.circle(screen, (255, 0, 0), (130, 700), 20, 0)
        # a11 = pygame.draw.circle(screen, (255, 0, 0), (60, 700), 20, 0)
        # a12 = pygame.draw.circle(screen, (255, 0, 0), (60, 630), 20, 0)
        # a13 = pygame.draw.circle(screen, (255, 0, 0), (60, 565), 20, 0)
        # a14 = pygame.draw.circle(screen, (255, 0, 0), (60, 505), 20, 0)
        # a15 = pygame.draw.circle(screen, (255, 0, 0), (60, 445), 20, 0)
        # a16 = pygame.draw.circle(screen, (255, 0, 0), (60, 380), 20, 0)
        # a17 = pygame.draw.circle(screen, (255, 0, 0), (60, 315), 20, 0)
        # a18 = pygame.draw.circle(screen, (255, 0, 0), (60, 250), 20, 0)
        # a19 = pygame.draw.circle(screen, (255, 0, 0), (60, 185), 20, 0)
        # a20 = pygame.draw.circle(screen, (255, 0, 0), (60, 120), 20, 0)
        # a21 = pygame.draw.circle(screen, (255, 0, 0), (60, 50), 20, 0)
        # a22 = pygame.draw.circle(screen, (255, 0, 0), (125, 50), 20, 0)
        # a23 = pygame.draw.circle(screen, (255, 0, 0), (190, 50), 20, 0)
        # a24 = pygame.draw.circle(screen, (255, 0, 0), (250, 50), 20, 0)
        # a25 = pygame.draw.circle(screen, (255, 0, 0), (310, 50), 20, 0)
        # a26 = pygame.draw.circle(screen, (255, 0, 0), (375, 50), 20, 0)
        # a27 = pygame.draw.circle(screen, (255, 0, 0), (440, 50), 20, 0)
        # a28 = pygame.draw.circle(screen, (255, 0, 0), (505, 50), 20, 0)
        # a29 = pygame.draw.circle(screen, (255, 0, 0), (570, 50), 20, 0)
        # a30 = pygame.draw.circle(screen, (255, 0, 0), (630, 50), 20, 0)
        # a31 = pygame.draw.circle(screen, (255, 0, 0), (700, 50), 20, 0)
        # a32 = pygame.draw.circle(screen, (255, 0, 0), (700, 125), 20, 0)
        # a33 = pygame.draw.circle(screen, (255, 0, 0), (700, 195), 20, 0)
        # a34 = pygame.draw.circle(screen, (255, 0, 0), (700, 255), 20, 0)
        # a35 = pygame.draw.circle(screen, (255, 0, 0), (700, 315), 20, 0)
        # a36 = pygame.draw.circle(screen, (255, 0, 0), (700, 375), 20, 0)
        # a37 = pygame.draw.circle(screen, (255, 0, 0), (700, 440), 20, 0)
        # a38 = pygame.draw.circle(screen, (255, 0, 0), (700, 505), 20, 0)
        # a39 = pygame.draw.circle(screen, (255, 0, 0), (700, 560), 20, 0)
        # a40 = pygame.draw.circle(screen, (255, 0, 0), (700, 625), 20, 0)

        pygame.display.flip()