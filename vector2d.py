# vector2d.py
import math

class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (float, int)):  # Scalar multiplication
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError(f"unsupported operand type(s) for *: 'Vector2D' and '{type(other).__name__}'")

    def __rmul__(self, other):
        # This ensures multiplication works in both directions
        return self.__mul__(other)

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        length = self.length()
        if length != 0:
            self.x /= length
            self.y /= length

    def distance_to(self, other):
        """Calculate the distance between two vectors."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    @staticmethod
    def from_angle(angle, magnitude=1):
        radian = math.radians(angle)
        return Vector2D(math.cos(radian) * magnitude, -math.sin(radian) * magnitude)
