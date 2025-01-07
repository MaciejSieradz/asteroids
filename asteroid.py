import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_angle_1 = self.velocity.rotate(angle)
        new_angle_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first = Asteroid(self.position.x, self.position.y, new_radius)
        second = Asteroid(self.position.x, self.position.y, new_radius)
        first.velocity = new_angle_1 * 1.2
        second.velocity = new_angle_2 * 1.2
