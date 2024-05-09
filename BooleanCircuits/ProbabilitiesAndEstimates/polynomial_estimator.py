from BooleanCircuits.CircuitConstruction.BooleanCircuit import BooleanCircuit
from BooleanCircuits.CircuitConstruction.BinaryGate import BinaryGate
from BooleanCircuits.CircuitPolynomialConstruction.CircuitMonomial import CircuitMonomial
from BooleanCircuits.CircuitPolynomialConstruction.CircuitPolynomial import CircuitPolynomial
from BooleanCircuits.CircuitPolynomialConstruction.create_polynomial_variables import create_polynomial_variables


one = CircuitMonomial(variables=[], coefficient=1)
one = CircuitPolynomial(monomials=[one])
zero = CircuitMonomial(variables=[], coefficient=0)
zero = CircuitPolynomial(monomials=[zero])

polynomial_operations = {'zero': lambda a, b: zero,
                         'one': lambda a, b: one,
                         'and': lambda a, b: a * b,
                         'or': lambda a, b: one - (one - a) * (one - b),
                         'xor': lambda a, b: a * (one - b) + (one - a) * b}


def polynomial_estimate(polynomial: CircuitPolynomial) -> int or float:
    output = 0
    for mono in polynomial.monomials:
        output += mono.coefficient * (1 / 2) ** len(mono.variables)
    return output


def polynomial_pass_through_gate(data_stream: tuple, gate: BinaryGate) -> CircuitPolynomial:
    a, b = data_stream[gate.indices[0]], data_stream[gate.indices[1]]
    estimate_op = polynomial_operations[gate.operation.name]
    return estimate_op(a, b)


def polynomial_pass_through_layer(data_stream: tuple, layer: list) -> tuple:
    return tuple([polynomial_pass_through_gate(data_stream, gate) for gate in layer])


def circuit_polynomial_estimate(boolean_circuit: BooleanCircuit) -> tuple or int or float:
    n = boolean_circuit.input_size
    data_stream = tuple(create_polynomial_variables(*[f"z{i}" for i in range(n)]))
    for layer in boolean_circuit.gate_layers:
        data_stream = polynomial_pass_through_layer(data_stream, layer)
    assert len(data_stream) == 1
    data_stream = data_stream[0]
    return polynomial_estimate(data_stream)
