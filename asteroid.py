import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: # Small Asteroid
            return
        random_angle = random.uniform(20,50)
        print(random_angle)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid_a.velocity = v1 * NEW_ASTEROID_VELOCITY_MULIPLIER
        new_asteroid_b.velocity = v2 * NEW_ASTEROID_VELOCITY_MULIPLIER

        