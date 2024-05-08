from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class CircuitVariable:
    rank: int
    name: str
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
