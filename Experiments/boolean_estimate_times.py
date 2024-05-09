from BooleanCircuits.CircuitConstruction.random_circuit import random_circuit
from BooleanCircuits.CircuitConstruction.BinaryOperation import BinaryOperation
from BooleanCircuits.ProbabilitiesAndEstimates.boolean_circuit_probability import (boolean_circuit_probability as
                                                                                   bool_prob)
from BooleanCircuits.ProbabilitiesAndEstimates.simple_estimator import simple_estimate
from BooleanCircuits.ProbabilitiesAndEstimates.polynomial_estimator import circuit_polynomial_estimate
import time


or_op = BinaryOperation(name='or')
and_op = BinaryOperation(name='and')
xor_op = BinaryOperation(name='xor')
binary_ops = [BinaryOperation(name='or'), BinaryOperation(name='and'), BinaryOperation(name='xor')]

bool_time = 0
simple_time = 0
poly_time = 0

simple_square_diff = 0
poly_square_diff = 0
for i in range(10):
    print("trial", i+1)
    circuit = random_circuit(input_size=5, binary_operations=binary_ops, max_layer_size=5)
    # timing calculation found at:
    # https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution

    start_time = time.time()
    bool_p = bool_prob(circuit)
    bool_time += (time.time() - start_time)

    start_time = time.time()
    simple_e = simple_estimate(circuit)
    simple_time += (time.time() - start_time)
    simple_square_diff += (bool_p - simple_e) ** 2

    start_time = time.time()
    poly_e = circuit_polynomial_estimate(circuit)
    poly_time += (time.time() - start_time)
    poly_square_diff += (bool_p - poly_e) ** 2

print(f"P(C) performance:\n- total time = {bool_time}\n")
print(f"simple E(C) performance:\n- total time = {simple_time}\n- sum of square difference = {simple_square_diff}\n")
print(f"poly E(C) performance:\n- total time = {poly_time}\n- sum of square difference = {poly_square_diff}\n")
