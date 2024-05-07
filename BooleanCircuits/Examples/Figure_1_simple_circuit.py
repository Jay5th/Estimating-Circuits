from BooleanCircuits.BooleanCircuit import BooleanCircuit
from BooleanCircuits.BinaryGate import BinaryGate
from BooleanCircuits.BinaryOperation import BinaryOperation
from BooleanCircuits.boolean_circuit_probability import boolean_circuit_probability as bool_prob
from BooleanCircuits.simple_estimator import simple_estimate

or_op = BinaryOperation(name='or')
and_op = BinaryOperation(name='and')
xor_op = BinaryOperation(name='xor')

# The following is an example of how to construct a boolean circuit using the classes I've implemented. Here, we
# construct the "simple boolean circuit" from Figure 1 of "Formalizing the presumption of independence".

gate_layers = []

layer0 = [BinaryGate(indices=(0, 1), operation=or_op),
          BinaryGate(indices=(0, 2), operation=xor_op),
          BinaryGate(indices=(1, 2), operation=or_op)]
gate_layers.append(layer0)

layer1 = [BinaryGate(indices=(0, 1), operation=and_op),
          BinaryGate(indices=(1, 2), operation=and_op)]
gate_layers.append(layer1)

layer2 = [BinaryGate(indices=(0, 1), operation=xor_op)]
gate_layers.append(layer2)

simple_boolean_circuit = BooleanCircuit(input_size=3, gate_layers=gate_layers)

data_input = (1, 1, 0)
print(f"{data_input} -> C ->", simple_boolean_circuit(data_input))
print("P(C) =", bool_prob(simple_boolean_circuit))
print("simple E(C) =", simple_estimate(simple_boolean_circuit))
