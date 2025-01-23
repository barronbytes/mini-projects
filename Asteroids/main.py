import pygame
from constants import *

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:

        # user clicked popup X to end game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # color over previous game frame
        screen.fill("black")

        # update display to show changes
        pygame.display.flip()



    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
