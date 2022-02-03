import pygame


class Window:
    def __init__(self):
        self.window = pygame.display.set_mode((800, 600))

    def set_window_fill(self):
        self.window.fill((24, 164, 240))

    def window_update(self):
        pygame.display.update()

    def window_make_character(self, image, cords):
        self.window.blit(image, cords)


window = Window()
