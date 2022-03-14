from vector import MyVector


class VectorBuilder:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.dim = -1

    def set_x(self, x):
        self.x = x
        return self

    def set_y(self, y):
        self.y = y
        return self

    def set_z(self, z):
        self.z = z
        return self

    def set_dim(self, dim):
        self.dim = dim
        return self

    def build(self):
        return MyVector(self.dim, self.x, self.y, self.z)


class VectorBuilder2D(VectorBuilder):
    def __init__(self):
        super().__init__()
        self.z = 0
        self.dim = 2

    def set_z(self, z):
        pass    # reject 3D function

    def set_dim(self, dim):
        pass    # reject dimension change


class VectorBuilder3D(VectorBuilder):
    def __init__(self):
        super().__init__()
        self.dim = 3

    def set_dim(self, dim):
        pass    # reject dimension change
