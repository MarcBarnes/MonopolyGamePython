import pygame
import thorpy

if __name__ == "__main__":
    application = thorpy.Application(size=(752, 754), caption="Monopoly")
    background = thorpy.Background(image="/Users/nicholasmeier/Desktop/monopoly.jpg")
    menu = thorpy.Menu(background)
    menu.play()
    application.quit()