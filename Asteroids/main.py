import pygame
from itertools import product
from constants import *
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from player_shot import PlayerShot


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
    shots_group = pygame.sprite.Group()
    Player.containers = (draw_group, update_group)
    PlayerShot.containers = (shots_group, draw_group, update_group)
    Asteroid.containers = (asteroids_group, draw_group, update_group)
    AsteroidField.containers = (update_group)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while running:

        # previous game frame
        screen.fill("black")

        # render new game (draw and update sprites)
        [sprite_obj.draw(screen) for sprite_obj in draw_group]
        [sprite_obj.update(dt) for sprite_obj in update_group]

        # game logic (collisions)
        for shot, asteroid in product(shots_group, asteroids_group):
            if shot.calc_collisions(asteroid):
                shot.kill()
                asteroid.kill()

        # update game display
        pygame.display.flip()

        # calculate delta time for next game frame
        dt = clock.tick(60) / 1000

        # end game
        end_by_user = any(
            event.type == pygame.QUIT or
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
            for event in pygame.event.get()
        )
        end_by_game = any(
            player.calc_collisions(asteroid)
            for asteroid in asteroids_group
        )
        running = False if (end_by_user == True or end_by_game == True) else True


if __name__ == "__main__":
    main()
