import pygame
import thorpy

if __name__ == "__main__":
    application = thorpy.Application(size=(752, 754), caption="Monopoly")
    #Make sure 'monopoly.jpg' is in the same working directory
    background = thorpy.Background(image=R"monopoly.jpg")
    menu = thorpy.Menu(background)
    menu.play()
    application.quit()
