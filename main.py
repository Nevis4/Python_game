import pygame
from Player import Player
from Game import Game


def main():
    player = Player()
    game = Game(player)
    pygame.init()
    game.play()


if __name__ == '__main__':
    main()
