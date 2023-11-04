# food.py
import pygame
import random
from physics_object import PhysicsObject, Vector2D
import uuid

class Food(PhysicsObject):
    def __init__(self, x, y, world,  radius=10):
        self.uuid = uuid.uuid4()
        x = random.randint(0, world.width)
        super().__init__(x, 0, world, radius)  # Food might have different mass        self.image = pygame.Surface((10, 10))
        self.color = (255, 0, 0)
        self.radius = radius



    def update(self):
        super().update()  # Call the parent update, which applies gravity and drag

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

        #
