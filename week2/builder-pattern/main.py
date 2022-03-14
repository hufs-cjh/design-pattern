from builder import *
from director import VectorDirector

builder_2d = VectorBuilder2D()
builder_3d = VectorBuilder3D()
director = VectorDirector()

# init 2D vectors
v_2d_ones = director.ones(builder_2d).build()
v_2d_something = builder_2d.set_x(2).set_y(4).build()

# init 3D vectors
v_3d_twos = director.twos(builder_3d).build()
v_3d_something = builder_3d.set_x(3).set_y(6).set_z(4).build()

multiplied_2d = v_2d_ones.get_scalar_multi(3)   # 2D Ones * 3 = (3, 3, 0)
print(f"2D ONES * 3 = ({multiplied_2d.x}, {multiplied_2d.y}, {multiplied_2d.z})")

v_2d_ones.plus(v_2d_something)                  # 2D Ones + (2, 4, 0) = (3, 5, 0)
print(f"2D ONES + (2, 4, 0) = ({v_2d_ones.x}, {v_2d_ones.y}, {v_2d_ones.z})")

multiplied_3d = v_3d_twos.get_scalar_multi(10)  # 3D Twos * 10 = (20, 20, 20)
print(f"3D TWOS * 10 = ({multiplied_3d.x}, {multiplied_3d.y}, {multiplied_3d.z})")

multiplied_3d.minus(v_3d_something)             # (3D Twos * 10) - (3, 6, 4) = (17, 14, 16)
print(f"(3D TWOS * 10) - (3, 6, 4) = ({multiplied_3d.x}, {multiplied_3d.y}, {multiplied_3d.z})")
