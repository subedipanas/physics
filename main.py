from scalar import Scalar
from unit import Unit
from units import Units
from expression import Expression, Term, TermSign

def main():
    a = Scalar(10, Units.m)
    b = Scalar(2, Units.m)
    c = Scalar(2, Units.m)
    d = Scalar(5, Units.kg)

    #term = Term()
    #term.add_factor(a)
    #term.add_factor(b.reciprocal())

    # exp = Expression()
    # exp.add_term(Term(TermSign.Plus, a))
    # exp.add_term(Term(TermSign.Plus, b))
    # exp.add_term(Term(TermSign.Minus, c))

    # print(exp)
    # print(exp.reduce())

if __name__ == "__main__":
    main()