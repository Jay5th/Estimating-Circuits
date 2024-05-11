from dataclasses import dataclass
from ArithmeticCircuits.CircuitConstruction.ArithmeticOperation import ArithmeticOperation


@dataclass(frozen=True)
class ArithmeticGate:
    indices: tuple[int, int]
    operation: ArithmeticOperation

    def __call__(self, data_input: tuple[float, ...]) -> float:
        a, b = data_input[self.indices[0]], data_input[self.indices[1]]
        return self.operation(a, b)
