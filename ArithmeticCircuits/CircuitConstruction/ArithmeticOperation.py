from dataclasses import dataclass


@dataclass(frozen=True)
class ArithmeticOperation:
    name: str = 'constant=0'

    def __call__(self, a: float, b: float) -> float:
        if self.name == 'sum':
            return a + b
        if self.name == 'product':
            return a * b
        return float(self.name[9:])
