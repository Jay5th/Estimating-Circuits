from BooleanCircuits.CircuitConstruction.BooleanCircuit import BooleanCircuit
from BooleanCircuits.CircuitConstruction.BinaryGate import BinaryGate

estimate_operations = {'zero': lambda a, b: 0,
                       'one': lambda a, b: 1,
                       'and': lambda a, b: a*b,
                       'or': lambda a, b: 1 - (1 - a)*(1 - b),
                       'xor': lambda a, b: a*(1 - b) + (1 - a)*b}


def estimate_pass_through_gate(data_stream: tuple, gate: BinaryGate) -> int or float:
    a, b = data_stream[gate.indices[0]], data_stream[gate.indices[1]]
    estimate_op = estimate_operations[gate.operation.name]
    return estimate_op(a, b)


def estimate_pass_through_layer(data_stream: tuple, layer: list) -> tuple:
    return tuple([estimate_pass_through_gate(data_stream, gate) for gate in layer])


def simple_estimate(boolean_circuit: BooleanCircuit) -> tuple or int or float:
    n = boolean_circuit.input_size
    data_stream = tuple([1/2 for i in range(n)])
    for layer in boolean_circuit.gate_layers:
        data_stream = estimate_pass_through_layer(data_stream, layer)
    if len(data_stream) == 1:
        data_stream = data_stream[0]
    return data_stream
