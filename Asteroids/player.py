import pygame
from constants import *
from circle_shape import CircleShape
from player_shot import PlayerShot


class Player(CircleShape):

    # initialize Player class instance (default radius)
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0 # rotation angle (in degrees)

    # override parent class
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)

    # override parent class
    def update(self, dt):
        keys = pygame.key.get_pressed()
    
        key_actions = {
            pygame.K_a: lambda: self.rotate(-dt),  # rotate left
            pygame.K_LEFT: lambda: self.rotate(-dt),  # rotate left
            pygame.K_d: lambda: self.rotate(dt),   # rotate right
            pygame.K_RIGHT: lambda: self.rotate(dt),   # rotate right
            pygame.K_w: lambda: self.move_forward(dt),  # move forward
            pygame.K_UP: lambda: self.move_forward(dt),  # move forward
            pygame.K_s: lambda: self.move_backward(dt),  # move backward
            pygame.K_DOWN: lambda: self.move_backward(dt),  # move backward
            pygame.K_SPACE: lambda: self.shot(), # generate shot
        }

        [action() for key, action in key_actions.items() if keys[key]]

    # calculate and return list of points for player triangle shape
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move_forward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def move_backward(self, dt):
        backward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += backward * PLAYER_SPEED * dt

    def shot(self):
        shot = PlayerShot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED
