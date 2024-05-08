from dataclasses import dataclass


@dataclass(frozen=True)
class CircuitVariable:
    name: str
    rank: int
