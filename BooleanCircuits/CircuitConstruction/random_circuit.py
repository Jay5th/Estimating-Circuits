from BooleanCircuits.CircuitConstruction.random_layer import random_layer
from BooleanCircuits.CircuitConstruction.BooleanCircuit import BooleanCircuit


def random_circuit(input_size: int, binary_operations: list, max_layer_size: int):
    current_input_size = input_size
    current_max_layer_size = max_layer_size
    gate_layers = []
    while current_input_size > 1:
        layer = random_layer(input_size=current_input_size, binary_operations=binary_operations,
                             max_layer_size=current_max_layer_size)
        gate_layers.append(layer)
        current_input_size = len(layer)
        current_max_layer_size -= 1
    return BooleanCircuit(input_size=input_size, gate_layers=gate_layers)
