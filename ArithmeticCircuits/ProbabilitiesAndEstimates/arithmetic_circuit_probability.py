import random
from ArithmeticCircuits.CircuitConstruction.ArithmeticCircuit import ArithmeticCircuit


def circuit_sample_mean_gaussian(circuit: ArithmeticCircuit, sample_size: int) -> float:
    sample_sum = 0
    for i in range(sample_size):
        data_input = tuple([random.gauss() for j in range(circuit.input_size)])
        sample_sum += circuit(data_input)
    return sample_sum / sample_size
