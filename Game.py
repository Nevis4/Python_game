import pygame
from Window import window
from Cash import Cash
pygame.font.init()

class Game:
    def __init__(self, player):
        self.__run = True
        self.player = player

    def play(self):
        clock = 0
        banknotes = []
        score = 0

        while self.__run:
            clock += pygame.time.Clock().tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__run = False
            if clock >= 3:
                banknotes.append(Cash())
                clock = 0

            text_image = pygame.font.Font.render(pygame.font.SysFont("arial", 48), str(score), True, (255, 255, 255)) # creating a score counter

            for banknote in banknotes:
                if self.player.hitbox.colliderect(banknote.hitbox):
                    banknotes.remove(banknote)
                    score += 1
                    print(score)

            window.set_window_fill()
            for banknote in banknotes:
                banknote.draw()

            self.player.move()
            window.window_make_character(text_image, (0, 0)) # draw counter
            window.window_update()


