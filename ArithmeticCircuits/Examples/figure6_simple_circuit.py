from ArithmeticCircuits.CircuitConstruction.ArithmeticOperation import ArithmeticOperation
from ArithmeticCircuits.CircuitConstruction.ArithmeticGate import ArithmeticGate
from ArithmeticCircuits.CircuitConstruction.ArithmeticCircuit import ArithmeticCircuit
from ArithmeticCircuits.ProbabilitiesAndEstimates.mean_propagation import mean_propagation

c1 = ArithmeticOperation(name="constant=1")
add_op = ArithmeticOperation(name="sum")
multiply_op = ArithmeticOperation(name="product")
input_first = ArithmeticOperation(name="first")

# The following is an example of how to construct an arithmetic circuit using the classes I've implemented. Here, we
# construct the "simple circuit" from Figure 6 of "Formalizing the presumption of independence".

layer0 = [ArithmeticGate(indices=(0, 0), operation=c1),
          ArithmeticGate(indices=(1, 1), operation=input_first),
          ArithmeticGate(indices=(2, 2), operation=input_first)]

layer1 = [ArithmeticGate(indices=(0, 1), operation=add_op),
          ArithmeticGate(indices=(0, 2), operation=add_op),
          ArithmeticGate(indices=(1, 2), operation=add_op)]

layer2 = [ArithmeticGate(indices=(0, 1), operation=multiply_op),
          ArithmeticGate(indices=(1, 2), operation=multiply_op)]

layer3 = [ArithmeticGate(indices=(0, 1), operation=add_op)]

simple_arithmetic_circuit = ArithmeticCircuit(input_size=3, gate_layers=[layer0, layer1, layer2, layer3])

if __name__ == '__main__':
    data_input = (1, 0, 0)
    print(f"{data_input} -> C ->", simple_arithmetic_circuit(data_input))
    print("E(C) ~", mean_propagation(circuit=simple_arithmetic_circuit))
