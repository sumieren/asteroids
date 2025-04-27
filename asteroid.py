import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def split(self):
        self.kill()

        #if small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = self.velocity.rotate(random_angle) * 1.2

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = self.velocity.rotate(-random_angle) * 1.2