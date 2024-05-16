import math

from typing import Self, Union
from scalar import Scalar
from errors import EmptyExpressionException

def get_significant_figures_after_decimal(value: Union[int, float]):
    if isinstance(value, int):
        return 0
    else:
        string_value = str(value)
        return len(string_value) - string_value.find(".") - 1

class TermSign:
    Plus = "+"
    Minus = "-"

class Term:
    def __init__(self: Self, sign: TermSign) -> None:
        self.sign = sign
        self.factors = []

    def add_factor(self: Self, factor: Union[Scalar]) -> None:
        self.factors.append(factor)

    def reduce(self: Self) -> Union[Scalar]:
        pass

    def __repr__(self: Self):
        return "{} {}".format(self.sign, self.quantity)

class Expression:
    def __init__(self: Self) -> None:
        self.terms = []

    def add_term(self: Self, term: Term) -> None:
        self.terms.append(term)

    def reduce(self: Self) -> Union[Scalar]:
        if len(self.terms) < 1: raise EmptyExpressionException

        min_sig_figures = math.inf

        reduction = self.terms[0].reduce() * (-1) if self.terms[0].sign == TermSign.Minus else self.terms[0].reduce()
        for counter in range(1, len(self.terms)):
            current_term = self.terms[counter]
            current_term_quantity = current_term.reduce()
            reduction = reduction + current_term_quantity if current_term.sign == TermSign.Plus else reduction - current_term_quantity

            sig_figures = get_significant_figures_after_decimal(current_term_quantity.value)
            min_sig_figures = min(min_sig_figures, sig_figures)

        return reduction.round(min_sig_figures)
    
    def __repr__(self: Self) -> Self:
        return " ".join([str(term) for term in self.terms])