import pygame
from Window import window
from random import randint


class Cash:
    def __init__(self):
        self.x_cord = randint(0, 800)
        self.y_cord = randint(0,600)
        self.wigth = 30
        self.height = 30
        self.image = pygame.image.load("img/cash.png")
        self.image = pygame.transform.scale(self.image, (self.wigth, self.height))
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.wigth, self.height)

    def draw(self):
        window.window_make_character(self.image, (self.x_cord, self.y_cord))

