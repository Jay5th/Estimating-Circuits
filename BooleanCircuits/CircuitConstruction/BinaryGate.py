from dataclasses import dataclass
from BooleanCircuits.CircuitConstruction.BinaryOperation import BinaryOperation


@dataclass(frozen=True)
class BinaryGate:
    indices: tuple[int, int]
    operation: BinaryOperation

    def __call__(self, data_input: tuple) -> int:
        a, b = data_input[self.indices[0]], data_input[self.indices[1]]
        return self.operation(a, b)
