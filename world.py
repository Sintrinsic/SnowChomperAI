# world.py
import pygame
class World:
    def __init__(self, width, height,  ground_height=50):
        self.width = width
        self.height = height
        self.ground_height = ground_height
        self.ground_level = self.height - self.ground_height
        self.ground_color = (52, 54, 49)  # A color that might represent the ocean floor, brownish.


    def draw(self, screen):
        """Draws the ground (ocean floor) on the screen."""
        pygame.draw.rect(screen, self.ground_color, pygame.Rect(0, self.ground_level, self.width, self.ground_height))
