import pygame
from constants import *
from circle_shape import CircleShape


class PlayerShot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, radius=SHOT_RADIUS)

    # override parent class
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    # override parent class
    def update(self, dt):
        self.position += self.velocity * dt
