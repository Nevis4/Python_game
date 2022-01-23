from Player import Player
import pygame


class Game:
    def __init__(self):
        self.run = True
        self.player = Player()

    def play(self):
        while self.run:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.player.window.fill((24, 164, 240))
            self.player.move()
            pygame.display.update()



game = Game()
pygame.init()
game.play()