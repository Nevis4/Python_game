import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wigth = 100
        self.height = 50
        self.player = pygame.rect.Rect(self.x, self.y, self.wigth, self.height)
    def move(self):
        keys = pygame.key.get_pressed()
        speed = 10
        if keys[pygame.K_RIGHT] and self.x < 800 - self.wigth:
            self.x += speed
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= speed
        if keys[pygame.K_DOWN] and self.y < 600 - self.height:
            self.y += speed

        self.player = pygame.rect.Rect(self.x, self.y, self.wigth, self.height)
