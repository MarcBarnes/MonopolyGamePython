import sys, pygame
pygame.init()

BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
YELLOW = (255, 255, 0)
GRAY = (211, 211, 211)
WHITE = (0, 0, 0)

class NumberPlayersButton(object):
    def __init__(self, btnText, xPos, yPos, width, height):
        self.btnText = btnText
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.btn = pygame.Surface((self.width, self.height))
        self.btn.fill(GRAY)
        self.rect = self.image.get_rect()

        font = pygame.font.Font('freesansbold.ttf', 15)
        text_image = font.render(self.btnText, True, WHITE)
        text_rect = text_image.get_rect(center = self.rect.center)

        blit(text_image, text_rect)
        self.rect.topleft = (self.xPos, self.yPos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        return self.btnText


if __name__ == "__main__":
    pygame.init()
    width, height = 752, 754
    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()
    is_running = False
    select2Players = NumberPlayersButton("2 Players", 20, 20, 40, 100)






    # bg = pygame.image.load("monopoly.jpg")
    #
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #     screen.blit(bg, [0, 0])
    #     a1 = pygame.draw.circle(screen, (255, 0, 0), (375, 55), 20, 0)
    #     pygame.display.flip()
