# food.py
import pygame
import random
from physics_object import PhysicsObject, Vector2D

class Food(PhysicsObject):
    def __init__(self, screen_width):
        x = random.randint(0, screen_width)
        super().__init__(x, 0, mass=1.0)  # Food might have different mass        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, 0))

    def update(self, screen_height):
        super().update()  # Call the parent update, which applies gravity and drag
        if self.rect.top > screen_height:
            self.kill()