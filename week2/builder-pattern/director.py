from builder import VectorBuilder


class VectorDirector:
    def zeros(self, builder: VectorBuilder):
        builder.set_x(0).set_y(0).set_z(0)
        return builder

    def ones(self, builder: VectorBuilder):
        builder.set_x(1).set_y(1).set_z(1)
        return builder

    def twos(self, builder: VectorBuilder):
        builder.set_x(2).set_y(2).set_z(2)
        return builder
