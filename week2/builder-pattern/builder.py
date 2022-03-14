from __future__ import annotations
from vector import MyVector


class VectorBuilder:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.dim = -1

    def set_x(self, x) -> VectorBuilder:
        self.x = x
        return self

    def set_y(self, y) -> VectorBuilder:
        self.y = y
        return self

    def set_z(self, z) -> VectorBuilder:
        self.z = z
        return self

    def set_dim(self, dim) -> VectorBuilder:
        self.dim = dim
        return self

    def build(self) -> MyVector:
        return MyVector(self.dim, self.x, self.y, self.z)


class VectorBuilder2D(VectorBuilder):
    def __init__(self):
        super().__init__()
        self.z = 0
        self.dim = 2

    def set_z(self, z) -> VectorBuilder:
        return self   # reject 3D function

    def set_dim(self, dim) -> VectorBuilder:
        return self    # reject dimension change


class VectorBuilder3D(VectorBuilder):
    def __init__(self):
        super().__init__()
        self.dim = 3

    def set_dim(self, dim) -> VectorBuilder:
        return self   # reject dimension change
