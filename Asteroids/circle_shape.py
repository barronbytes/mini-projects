import pygame
from abc import ABC, abstractmethod


# base class for circular game objects, abstract class
class CircleShape(pygame.sprite.Sprite, ABC):

    # initialize CircleShape class instance
    def __init__(self, x, y, radius):

        # initialize Sprite class from parent class
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0) # stationary by default
        self.radius = radius

    @abstractmethod
    def draw(self, screen):
        pass # must override

    @abstractmethod
    def update(self, dt):
        pass # must override
    