from Player import Player
import pygame


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((800, 600))
        self.run = True
        self.player = Player()

    def play(self):

        while self.run:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.player.move()
            self.window.fill((24, 164, 240))
            pygame.draw.rect(self.window, (20, 200, 20), self.player.player)
            pygame.display.update()



game = Game()
pygame.init()
game.play()
