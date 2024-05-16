from typing import Self

class TypeMismatchException(Exception):
    def __init__(self) -> None:
        message = "Type mismatch. Cannot complete operation"
        super().__init__(message)

class EmptyExpressionException(Exception):
    def __init__(self) -> None:
        message = "Empty Expression. Cannot complete operation"
        super().__init__(message)

class UnitMismatchException(Exception):
    def __init__(self: Self) -> None:
        message="Unit mismatch. Cannot complete operation"
        super().__init__(message)

class InvalidUnitDefinition(Exception):
    def __init__(self) -> None:
        message = "Invalid unit definition. Provide only one of: symbol, components."
        super().__init__(message)