# player.py
import pygame
from physics_object import PhysicsObject, Vector2D
import math


class Player(PhysicsObject):
    def __init__(self, x, y, world, radius=10, mass=1.0):
        super().__init__(x, y, world, mass)
        self.radius = radius
        self.energy = 100
        self.thrust_strength = 5
        self.rotation_speed = 30  # degrees per frame

    def rotate_left(self):
        self.angle += self.rotation_speed
        self.angle = self.angle % 360  # Ensure angle stays within 0-359 degrees

    def rotate_right(self):
        self.angle -= self.rotation_speed
        self.angle = self.angle % 360  # Ensure angle stays within 0-359 degrees

    def thrust(self):
        if self.energy > 0:
            # Get the normalized direction vector and apply thrust
            direction_vector = self.get_normalized_direction_vector()
            thrust_vector = direction_vector * self.thrust_strength
            self.add_velocity_vector(thrust_vector)
            self.energy -= 10  # Consume energy

    def draw(self, screen):
        # Draw the player as a circle
        pygame.draw.circle(screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), self.radius)

        # Draw the direction line
        direction_vector = self.get_normalized_direction_vector()
        line_end = self.position + direction_vector * self.radius
        pygame.draw.line(screen, (255, 0, 0), (self.position.x, self.position.y), (line_end.x, line_end.y), 2)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.thrust()
                print("thrusting")
            if event.key == pygame.K_a:
                self.rotate_left()
                print("turning left_")
            if event.key == pygame.K_d:
                self.rotate_right()
                print("turning right")

    def update(self):
        super().update()
