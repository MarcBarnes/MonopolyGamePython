import sys, pygame
pygame.init()

BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
YELLOW = (255, 255, 0)


class Player:
    def _init_(self, number):
        self.position = None
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
    playerOne = Player.__init__(1)
    playerTwo = Player.__init__(2)
    playerThree = Player.__init__(3)
    playerFour = Player.__init__(4)

    width, height = 752, 754
    screen = pygame.display.set_mode((width, height))

    bg = pygame.image.load("monopoly.jpg")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, [0,0])

        # if playerOne.position == 1:
        #     a1 = pygame.draw.circle(screen, (255, 0, 0), (700, 700), 20, 0)

        a1 = pygame.draw.circle(screen, (255,0,0), (700, 700), 20, 0)
        a2 = pygame.draw.circle(screen, (255, 0, 0), (630, 700), 20, 0)
        a3 = pygame.draw.circle(screen, (255, 0, 0), (565, 700), 20, 0)
        a4 = pygame.draw.circle(screen, (255, 0, 0), (500, 700), 20, 0)
        a5 = pygame.draw.circle(screen, (255, 0, 0), (440, 700), 20, 0)
        a6 = pygame.draw.circle(screen, (255, 0, 0), (380, 700), 20, 0)
        a7 = pygame.draw.circle(screen, (255, 0, 0), (315, 700), 20, 0)
        a8 = pygame.draw.circle(screen, (255, 0, 0), (255, 700), 20, 0)
        a9 = pygame.draw.circle(screen, (255, 0, 0), (190, 700), 20, 0)
        a10 = pygame.draw.circle(screen, (255, 0, 0), (130, 700), 20, 0)
        a11 = pygame.draw.circle(screen, (255, 0, 0), (60, 700), 20, 0)
        a12 = pygame.draw.circle(screen, (255, 0, 0), (60, 630), 20, 0)
        a13 = pygame.draw.circle(screen, (255, 0, 0), (60, 565), 20, 0)
        a14 = pygame.draw.circle(screen, (255, 0, 0), (60, 505), 20, 0)
        a15 = pygame.draw.circle(screen, (255, 0, 0), (60, 445), 20, 0)
        a16 = pygame.draw.circle(screen, (255, 0, 0), (60, 380), 20, 0)
        a17 = pygame.draw.circle(screen, (255, 0, 0), (60, 315), 20, 0)
        a18 = pygame.draw.circle(screen, (255, 0, 0), (60, 250), 20, 0)
        a19 = pygame.draw.circle(screen, (255, 0, 0), (60, 185), 20, 0)
        a20 = pygame.draw.circle(screen, (255, 0, 0), (60, 120), 20, 0)
        a21 = pygame.draw.circle(screen, (255, 0, 0), (60, 50), 20, 0)
        a22 = pygame.draw.circle(screen, (255, 0, 0), (125, 50), 20, 0)
        a23 = pygame.draw.circle(screen, (255, 0, 0), (190, 50), 20, 0)
        a24 = pygame.draw.circle(screen, (255, 0, 0), (250, 50), 20, 0)
        a25 = pygame.draw.circle(screen, (255, 0, 0), (310, 50), 20, 0)
        a26 = pygame.draw.circle(screen, (255, 0, 0), (375, 50), 20, 0)
        a27 = pygame.draw.circle(screen, (255, 0, 0), (440, 50), 20, 0)
        a28 = pygame.draw.circle(screen, (255, 0, 0), (505, 50), 20, 0)
        a29 = pygame.draw.circle(screen, (255, 0, 0), (570, 50), 20, 0)
        a30 = pygame.draw.circle(screen, (255, 0, 0), (630, 50), 20, 0)
        a31 = pygame.draw.circle(screen, (255, 0, 0), (700, 50), 20, 0)
        a32 = pygame.draw.circle(screen, (255, 0, 0), (700, 125), 20, 0)
        a33 = pygame.draw.circle(screen, (255, 0, 0), (700, 195), 20, 0)
        a34 = pygame.draw.circle(screen, (255, 0, 0), (700, 255), 20, 0)
        a35 = pygame.draw.circle(screen, (255, 0, 0), (700, 315), 20, 0)
        a36 = pygame.draw.circle(screen, (255, 0, 0), (700, 375), 20, 0)
        a37 = pygame.draw.circle(screen, (255, 0, 0), (700, 440), 20, 0)
        a38 = pygame.draw.circle(screen, (255, 0, 0), (700, 505), 20, 0)
        a39 = pygame.draw.circle(screen, (255, 0, 0), (700, 560), 20, 0)
        a40 = pygame.draw.circle(screen, (255, 0, 0), (700, 625), 20, 0)

        pygame.display.flip()