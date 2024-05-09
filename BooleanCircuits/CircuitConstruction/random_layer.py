from random import randint
from BooleanCircuits.CircuitConstruction.BinaryGate import BinaryGate


def random_layer(input_size: int, binary_operations: list, max_layer_size: int) -> list:
    layer_size = randint(1, max_layer_size)
    layer = []
    for k in range(layer_size):
        i = randint(0, input_size-1)
        j = randint(0, input_size-1)
        if j == i:
            j = (j + 1) % input_size
        binary_op = binary_operations[randint(0, len(binary_operations)-1)]
        layer.append(BinaryGate(indices=(i, j), operation=binary_op))
    return layer
