import pygame
from circleshape import CircleShape

from constants import LINE_WIDTH


class Shot(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH,
        )

    def update(self, dt):
        self.position += self.velocity * dt
