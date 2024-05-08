from dataclasses import dataclass


@dataclass(frozen=True)
class CircuitVariable:
    name: str
    rank: int

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
