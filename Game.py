import pygame
from Window import window
from Cash import Cash


class Game:
    def __init__(self, player):
        self.__run = True
        self.player = player

    def play(self):
        __clock = 0
        __banknotes = []
        __score = 0

        while self.__run:
            __clock += pygame.time.Clock().tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__run = False
            if __clock >= 3:
                __banknotes.append(Cash())
                __clock = 0

            for banknote in __banknotes:
                if self.player.hitbox.colliderect(banknote.hitbox):
                    __banknotes.remove(banknote)
                    __score += 1
                    print(__score)

            window.set_window_fill()
            for banknote in __banknotes:
                banknote.draw()

            self.player.move()
            window.window_update()


