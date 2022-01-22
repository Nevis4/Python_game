import pygame


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((800, 600))
        self.x = 0
        self.y = 0
        self.player = pygame.rect.Rect(self.x, self.y, 100, 100)
        self.run = True

    def play(self):

        while self.run:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            keys = pygame.key.get_pressed()
            speed = 10
            if keys[pygame.K_RIGHT] and self.x < 800 - 100:
                self.x += speed
            if keys[pygame.K_LEFT] and self.x > 0:
                self.x -= speed
            if keys[pygame.K_UP] and self.y > 0:
                self.y -= speed
            if keys[pygame.K_DOWN] and self.y < 600 - 100:
                self.y += speed

            self.player = pygame.rect.Rect(self.x, self.y, 100, 100)

            self.window.fill((24, 164, 240))
            pygame.draw.rect(self.window, (20, 200, 20), self.player)
            pygame.display.update()


game = Game()
pygame.init()
game.play()
