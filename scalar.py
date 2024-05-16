from typing import Self, Union
from unit import Unit
from errors import UnitMismatchException

class Scalar:
    def __init__(self: Self, value: str, unit: Unit) -> None:
        self.value = value
        self.unit = unit

    def round(self: Self, sig_figures) -> Self:
        return Scalar(round(self.value, sig_figures), self.unit)
    
    def reciprocal(self: Self) -> Self:
        return Scalar(1/self.value, self.unit.reciprocal())

    def __add__(self: Self, other: Self) -> Self:
        if self.unit != other.unit: raise UnitMismatchException
        return Scalar(self.value + other.value, self.unit)
    
    def __sub__(self: Self, other: Self) -> Self:
        if self.unit != other.unit: raise UnitMismatchException
        return Scalar(self.value - other.value, self.unit)
    
    def __mul__(self: Self, other: Union[Self, int, float]) -> Self:
        if isinstance(other, self.__class__):
            return Scalar(self.value * other.value, self.unit * other.unit)
        else:
            return Scalar(self.value * other, self.unit)
    
    def __truediv__(self: Self, other: Self) -> Self:
        return Scalar(self.value / other.value, self.unit / other.unit)
    
    def __floordiv__(self: Self, other: Self) -> Self:
        return Scalar(int(self.value // other.value), self.unit / other.unit)
    
    def __mod__(self: Self, other: Self) -> Self:
        return Scalar(self.value % other.value, self.unit)
    
    def __repr__(self: Self):
        return "{} {}".format(self.value, self.unit)