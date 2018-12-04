import sys, pygame
pygame.init()

BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
YELLOW = (255, 255, 0)


if __name__ == "__main__":
    width, height = 752, 754
    screen = pygame.display.set_mode((width, height))

    bg = pygame.image.load("monopoly.jpg")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, [0, 0])
        a1 = pygame.draw.circle(screen, (255, 0, 0), (375, 55), 20, 0)
        pygame.display.flip()
