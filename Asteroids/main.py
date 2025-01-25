import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # refers to delta time
    running = True

    # sprite setup
    draw_group = pygame.sprite.Group()
    update_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    Player.containers = (draw_group, update_group)
    Asteroid.containers = (asteroids_group, draw_group, update_group)
    AsteroidField.containers = (update_group)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while running:

        # user clicked X on popup or Esc key to end game
        running = not any(
            event.type == pygame.QUIT or 
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
            for event in pygame.event.get()
        )

        # color over previous game frame
        screen.fill("black")

        # render game
        [sprite_obj.draw(screen) for sprite_obj in draw_group]
        [sprite_obj.update(dt) for sprite_obj in update_group]

        # update display to show changes
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
