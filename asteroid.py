import pygame
from circleshape import CircleShape
from typing import Optional, Tuple
from constants import *
import random


class Asteroid(CircleShape):

    _containers: Optional[
        Tuple[pygame.sprite.Group, pygame.sprite.Group, pygame.sprite.Group]
    ] = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        if Asteroid._containers is not None:
            for group in Asteroid._containers:
                group.add(self)

        return

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

        return

    def update(self, dt):
        self.position += self.velocity * dt
        return

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_v1 = self.velocity.rotate(new_angle)
        new_v2 = self.velocity.rotate(-new_angle)
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_v1 * 1.2
        asteroid_2.velocity = new_v2 * 1.2

        if Asteroid._containers is not None:
            for group in Asteroid._containers:
                group.add(asteroid_2)
                group.add(asteroid_1)
