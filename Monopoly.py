import sys, pygame, random
from pygame.locals import *
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
    def __init__(self, number):
        self.position = random.randint(1,40)
        self.number = number

        if self.number == 1:
            self.pawnColor = BLUE
        if self.number == 2:
            self.pawnColor = GREEN
        if self.number == 3:
            self.pawnColor = RED
        if self.number == 4:
            self.pawnColor = YELLOW


if __name__ == "__main__":
    players = []                #array of players
    playerOne = Player(1)
    playerTwo = Player(2)
    playerThree = Player(3)
    playerFour = Player(4)
    width, height = 752, 800    #set size of the window. The size of the image is 752,754 but I went to 800 to add space for buttons
    screen = pygame.display.set_mode((width, height))
    startButton = button((0, 255, 255), 752/2 - 50, 754/2 - 50, 100, 50, "Start")
    bg = pygame.image.load("monopoly.jpg")
    gameHasStarted = False                              #initialize that the game hasnt started
    numPlayersChosen = False                            #initialize that number of players hasnt been chosen
    numPlayers = 0                                      #intialized to 0 for no reason, just to have value
    running = True
    print("Started Running main loop")
    while running:
        screen.blit(bg, [0, 0])
        print("Painting Background")
        for event in pygame.event.get():                #end python interpretter if window has been closed
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:    #start has been pushed
                if startButton.isOver(pos):
                    gameHasStarted = True
                    print("Game has started")

        if gameHasStarted == False:
            print("Drawing start button")
            startButton.draw(screen)

        if gameHasStarted:
            if numPlayersChosen == False:
                print("Drawing howManyPlayers text")
                pressedKey = pygame.key.get_pressed()
                howManyPlayers = button((0, 0, 0), 752/2, 754/4 * 3 - 50, 0, 0, "How many Players?(1-4)")
                howManyPlayers.draw(screen)
                if pressedKey[K_1]:
                    numPlayers = 1
                    numPlayersChosen = True

                if pressedKey[K_2]:
                    numPlayers = 2
                    numPlayersChosen = True

                if pressedKey[K_3]:
                    numPlayers = 3
                    numPlayersChosen = True

                if pressedKey[K_4]:
                    numPlayers = 4
                    numPlayersChosen = True

            if numPlayersChosen:
                

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
        #flip and update go last always
        pygame.display.flip()
        pygame.display.update()