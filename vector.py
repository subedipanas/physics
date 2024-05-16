from math import sin, cos, sqrt, atan, inf, acos, degrees

from typing import Self, Union
from unit import Unit
from errors import UnitMismatchException, TypeMismatchException

BOLD = "\033[1m"
END = "\033[0m"
ITALICS = '\033[3m'

class Vector:
    """
        value = magnitude
        x, y, z = components
        directions = (phi, theta)
            phi = angle from positive x-axis in the XY plane
            theta = angle from positive x-axis to the XZ plane
    """
    def __init__(self: Self, unit: Unit, value: float = None, direction: tuple = (0, 0), x: float = None, y: float = None, z: float = None) -> None:
        self.direction = direction
        self.unit = unit
        self.value = value
        self.x = x
        self.y = y
        self.z = z

        if self.x is not None and self.y is not None and self.z is not None:
            self.calculate_value()
        elif self.value is not None:
            self.calculate_components()
    
    def __repr__(self: Self):
        return "{}{}{}{} {}".format(BOLD, ITALICS, self.value, END, self.unit)
    
    def print(self: Self, round_digits: int = 2) -> None:
        print("{}x + {}y + {}z".format(round(self.x, round_digits), round(self.y, round_digits), round(self.z, round_digits)))
    
    def calculate_value(self: Self):
        self.value = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

        direction = [0, 0]
        direction[0] = atan(self.y * inf) if self.x == 0 else atan(self.y/self.x)
        direction[1] = atan(self.z * inf) if self.x == 0 else atan(self.z/self.x)
        self.direction = direction

    def calculate_components(self: Self):
        self.x = self.value * cos(self.direction[0])
        self.y = self.value * sin(self.direction[0])
        self.z = self.value * sin(self.direction[1])
    
    def reciprocal(self: Self) -> Self:
        return Vector(1/self.value, self.unit.reciprocal())
    
    def angle(self: Self, other: Self, unit: str = "radian") -> float:
        result = acos(self * other / (self.value * other.value))
        return degrees(result) if unit == "degree" else result
    
    def cross(self: Self, other: Self) -> Self:
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x

        return Vector(unit=self.unit * other.unit, x=x, y=y, z=z)
    
    def __add__(self: Self, other: Self) -> Self:
        if self.unit != other.unit: raise UnitMismatchException

        if isinstance(other, self.__class__):
            return Vector(unit=self.unit, x=self.x+other.x, y=self.y+other.y, z=self.z+other.z)
        
        else:
            raise TypeMismatchException

    def __sub__(self: Self, other: Self) -> Self:
        if self.unit != other.unit: raise UnitMismatchException

        if isinstance(other, self.__class__):
            return Vector(unit=self.unit, x=self.x-other.x, y=self.y-other.y, z=self.z-other.z)
        else:
            raise TypeMismatchException
        
    def __mul__(self: Self, other: Union[Self, float, int]) -> Union[Self, float]:
        if isinstance(other, self.__class__):
            # scalar product
            return float(self.x * other.x + self.y * other.y + self.z * other.z)

        elif isinstance(other, int) or isinstance(other, float):
            return Vector(unit=self.unit, x=self.x*other, y=self.y*other, z=self.z*other)