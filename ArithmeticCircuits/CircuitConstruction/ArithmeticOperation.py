from dataclasses import dataclass


@dataclass(frozen=True)
class ArithmeticOperation:
    name: str = 'first'

    def __call__(self, a: float, b: float) -> float:
        if self.name == 'sum':
            return a + b
        if self.name == 'product':
            return a * b
        if self.name[0:8] == 'constant':
            return float(self.name[9:])
        if self.name == 'first':
            return a
        if self.name == 'last':
            return b
        else:
            raise ValueError(f"an arithmetic operation named {self.name} has not been implemented")
