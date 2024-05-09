from dataclasses import dataclass


@dataclass(order=True)
class CircuitMonomial:
    variables: list
    coefficient: int

    def __init__(self, variables: list, coefficient: int):
        self.variables = sorted(variables, key=lambda a: a.rank)
        self.coefficient = coefficient

    def __str__(self):
        if self.coefficient == 0:
            return "0"
        if len(self.variables) == 0:
            return str(self.coefficient)
        if self.coefficient == 1:
            return "*".join([str(var) for var in self.variables])
        return str(self.coefficient) + "*".join([str(var) for var in self.variables])

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        if (self.coefficient == 0) or (other.coefficient == 0):
            return CircuitMonomial(coefficient=0, variables=[])
        combined_variables = list(set(self.variables) | set(other.variables))
        return CircuitMonomial(coefficient=self.coefficient * other.coefficient,
                               variables=combined_variables)
