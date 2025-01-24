import pygame
from constants import *
from player import Player

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # refers to delta time
    running = True

    # player setup
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while running:

        # user clicked popup X to end game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # color over previous game frame
        screen.fill("black")

        # render game
        player.draw(screen)
        player.update(dt)

        # update display to show changes
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
