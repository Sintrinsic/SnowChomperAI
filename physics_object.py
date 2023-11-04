# physics_object.py
import pygame
from vector2d import Vector2D
import math

class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, x, y,  world, radius, mass=1.0):
        super().__init__()
        self.world = world
        self.angle = 180
        self.radius = radius
        self.position = Vector2D(x, y)
        self.velocity = Vector2D(0,0)
        self.gravity = Vector2D(0, 0.1)  # The force of gravity as a vector
        self.drag_coefficient = 0.99  # Drag coefficient

    def apply_physics(self):
        # Apply gravity as a constant force
        new_vector = self.drag_coefficient * (self.velocity + self.gravity)
        new_vector = self.check_colision(self.world, new_vector)
        self.position = self.position + new_vector
        self.velocity = new_vector

    def check_colision(self, world, new_vector):
        if self.position.y > world.ground_level and new_vector.y > 0:
            self.position.y = world.ground_level
            new_vector.y = 0

        if self.position.y < 0:
            self.position.y = 0
            new_vector.y = 0

        if self.position.x > world.width:
            self.position.x = world.width
            new_vector.x = 0

        if self.position.x < 0:
            self.position.x = 0
            new_vector.x = 0

        return new_vector


    def collide_with_object(self, other_object):
        # Calculate the distance between the centers of the two objects
        distance = self.position.distance_to(other_object.position)

        # Check if the distance is less than the sum of the radii
        return distance < (self.radius + other_object.radius)

    def set_velocity(self, velocity):
        self.velocity = velocity

    def add_velocity_vector(self, velocity):
        self.velocity = self.velocity + velocity

    def get_normalized_direction_vector(self):
        # Convert angle to radians
        angle_in_radians = math.radians(self.angle)

        # Adjust angle to point upwards for 0 degrees and convert to Pygame coordinate system
        # Subtract 90 degrees (or π/2 radians) to make 0 degrees point upwards
        # Invert y-component by subtracting it from π to flip the y-axis
        angle_in_radians -= math.pi / 2

        # Calculate vector components
        x = math.cos(angle_in_radians)
        y = math.sin(angle_in_radians)

        # Create a normalized vector
        direction_vector = Vector2D(x, -y)  # Invert y to match screen coordinates (y increases downwards)
        direction_vector.normalize()

        return direction_vector
    def update(self):
        self.apply_physics()

