from BooleanCircuits.ProbabilitiesAndEstimates.binary_sequences import binary_sequences
from BooleanCircuits.CircuitConstruction.BooleanCircuit import BooleanCircuit


def boolean_circuit_probability(boolean_circuit: BooleanCircuit) -> float:
    n = boolean_circuit.input_size
    possible_inputs = binary_sequences(sequence_length=n)
    one_count = 0
    for data_input in possible_inputs:
        one_count += boolean_circuit(data_input)
    return one_count / 2**n
