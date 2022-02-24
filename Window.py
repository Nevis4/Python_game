import pygame


class Window:
    def __init__(self):
        self.window = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load("img/bacground.jpg")
        self.text_image = 0

    def set_window_fill(self):
        self.window.blit(self.background, (-200, -200))

    def window_update(self):
        pygame.display.update()

    def window_make_character(self, image, cords):
        self.window.blit(image, cords)


window = Window()
