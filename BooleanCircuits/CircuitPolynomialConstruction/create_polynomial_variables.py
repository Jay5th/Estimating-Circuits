from BooleanCircuits.CircuitPolynomialConstruction.CircuitVariable import CircuitVariable
from BooleanCircuits.CircuitPolynomialConstruction.CircuitMonomial import CircuitMonomial
from BooleanCircuits.CircuitPolynomialConstruction.CircuitPolynomial import CircuitPolynomial


def create_polynomial_variables(*names: str) -> list:
    poly_variables = []
    for i in range(len(names)):
        var_i = CircuitVariable(name=names[i], rank=i)
        mono_i = CircuitMonomial(variables=[var_i], coefficient=1)
        poly_i = CircuitPolynomial(monomials=[mono_i])
        poly_variables.append(poly_i)
    return poly_variables
