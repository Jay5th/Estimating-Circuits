from dataclasses import dataclass
from BooleanCircuits.CircuitPolynomialConstruction.CircuitMonomial import CircuitMonomial


@dataclass(order=True)
class CircuitPolynomial:
    monomials: list

    def __init__(self, monomials: list):
        self.monomials = sorted(monomials, key=lambda mono: [var.rank for var in mono.variables])

    def __str__(self):
        if len(self.monomials) == 0:
            return "0"
        output_str = ""
        for i in range(len(self.monomials)):
            mono = self.monomials[i]
            if i == 0:
                output_str += str(mono)
            elif mono.coefficient < 0:
                temp_str = str(mono)
                temp_str = temp_str.replace("-", " - ")
                output_str += temp_str
            else:
                output_str += " + " + str(mono)
        return output_str

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = CircuitMonomial(variables=[], coefficient=other)
            other = CircuitPolynomial([other])
        new_monomials_info = {}
        for mono in self.monomials + other.monomials:
            if tuple(mono.variables) in new_monomials_info.keys():
                new_monomials_info[tuple(mono.variables)] += mono.coefficient
            else:
                new_monomials_info[tuple(mono.variables)] = mono.coefficient
        new_monomials = []
        for variables, coefficient in new_monomials_info.items():
            new_monomials.append(CircuitMonomial(variables=list(variables), coefficient=coefficient))
        return CircuitPolynomial(monomials=new_monomials)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = CircuitMonomial(variables=[], coefficient=other)
            other = CircuitPolynomial([other])
        new_monomials = [mono_i * mono_j for mono_i in self.monomials for mono_j in other.monomials]
        return CircuitPolynomial(monomials=new_monomials)

    def __sub__(self, other):
        return self + other * (-1)

    def __neg__(self):
        return self * (-1)
