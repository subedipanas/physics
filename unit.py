from typing import Self, Union, List
from errors import InvalidUnitDefinition

# index = ["-", "2", "3", "4"]
superscript = ["\u207b", "\u00b9", "\u00b2", "\u00b3", "s4"]

class Unit:
    def __init__(self: Self, symbol: str = None, degree: int = 1, components: List[Self] = []) -> None:
        self.components = components
        self.degree = degree
        self.symbol = symbol

    def reciprocal(self: Self) -> Self:
        if len(self.components) > 0:
            return Unit(components=[Unit(symbol=unit.symbol, degree=unit.degree*(-1)) for unit in self.components])
        else:
            return Unit(symbol=self.symbol, degree=self.degree*(-1))

    def __repr__(self: Self) -> str:
        if self.symbol is not None:
            if self.degree == 0:
                return ""
            elif self.degree == 1:
                return "{}".format(self.symbol)
            elif self.degree > 1:
                return "{}{}".format(self.symbol, superscript[self.degree])
            else:
                return "{}{}{}".format(self.symbol, superscript[0], superscript[self.degree*(-1)])
            
        else:
            if len(self.components) < 1:
                raise Exception("Invalid unit. No symbol or components defined.")
            return "".join([str(component) for component in self.components])
    
    def __eq__(self: Self, other: Self) -> bool:
        return self.symbol == other.symbol and self.degree == other.degree
    
    def __truediv__(self: Self, other: Self) -> Self:
        if len(self.components + other.components) == 0:
            if self.symbol == other.symbol:
                if self.degree == other.degree:
                    return Unit(symbol=self.symbol, degree=0, components=[])
                else:
                    return Unit(symbol=self.symbol, degree=self.degree - other.degree)
            else:
                return Unit(components=[self, Unit(symbol=other.symbol, degree=other.degree*(-1))])
            
        if len(self.components) == 0 and len(other.components) > 0:
            components = [self, ] + [Unit(symbol=unit.symbol, degree=unit.degree*(-1)) for unit in other.components]
        
        if len(self.components) > 0 and len(other.components) == 0:
            components = self.components + [Unit(symbol=other.symbol, degree=other.degree*(-1)), ]
        
        if len(self.components) > 0 and len(other.components) > 0:
            components = self.components + [Unit(symbol=unit.symbol, degree=unit.degree*(-1)) for unit in other.components]

        units = {}
        for unit in components:
            units[unit.symbol] = units.get(unit.symbol, 0) + unit.degree

        new_units = []
        for unit in units:
            new_units.append(Unit(symbol=unit, degree=units[unit]))
            
        return Unit(components=new_units)
    
    def __mul__(self: Self, other: Self) -> Self:
        if len(self.components + other.components) == 0:
            if self.symbol == other.symbol:
                return Unit(symbol=self.symbol, degree=self.degree + other.degree)
            else:
                return Unit(components=[self, other])
            
        if len(self.components) == 0 and len(other.components) > 0:
            components = [self, ] + other.components
        
        if len(self.components) > 0 and len(other.components) == 0:
            components = self.components + [other, ]
        
        if len(self.components) > 0 and len(other.components) > 0:
            components = self.components + other.components

        units = {}
        for unit in components:
            units[unit.symbol] = units.get(unit.symbol, 0) + unit.degree

        new_units = []
        for unit in units:
            new_units.append(Unit(symbol=unit, degree=units[unit]))
            
        return Unit(components=new_units)
        
