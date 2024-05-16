from math import radians, pi

from scalar import Scalar
from vector import Vector
from unit import Unit
from units import Units

def main():
    # a = Scalar(0.75, Units.m)
    # b = Scalar(2, Units.m)
    # c = Scalar(2, Units.m)
    # d = Scalar(5, Units.kg)


    # print(a.reciprocal() * b)

    a = Vector(unit=Units.N, value=6, direction=(0, 0))
    b = Vector(unit=Units.N, value=4, direction=(radians(30), 0))
    c = b.cross(a)

    a.print()
    b.print()

    print(c)
    c.print()

if __name__ == "__main__":
    main()