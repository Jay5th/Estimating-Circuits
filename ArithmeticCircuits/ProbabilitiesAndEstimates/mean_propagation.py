from ArithmeticCircuits.CircuitConstruction.ArithmeticCircuit import ArithmeticCircuit


def mean_propagation(circuit: ArithmeticCircuit):
    return circuit(tuple([0 for i in range(circuit.input_size)]))
