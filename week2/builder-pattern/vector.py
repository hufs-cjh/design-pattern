from __future__ import annotations
import math
import copy


class MyVector:
    def __init__(self, dim, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dim = dim
        self.dist = 0

    def normalize(self) -> MyVector:
        mag = self.get_magnitude()
        self.x /= mag
        self.y /= mag
        self.z /= mag
        return self

    def get_magnitude(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def get_state(self):
        return self.x, self.y, self.z

    def get_scalar_multi(self, scalar: int) -> MyVector:
        copied = copy.deepcopy(self)
        copied.x *= scalar
        copied.y *= scalar
        copied.z *= scalar

        return copied

    def plus(self, vector: MyVector) -> MyVector:
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        return self

    def minus(self, vector: MyVector) -> MyVector:
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z
        return self
