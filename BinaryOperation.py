from dataclasses import dataclass

current_options = {'zero', 'one', 'and', 'or', 'xor'}


@dataclass(frozen=True)
class BinaryOperation:
    name: str = 'zero'
    assert name in current_options, f"I have not implemented a binary operation named {name}."
    if name == 'zero':
        def __call__(self, a: int, b: int) -> int:
            return 0
    elif name == 'one':
        def __call__(self, a: int, b: int) -> int:
            return 1
    elif name == 'and':
        def __call__(self, a: int, b: int) -> int:
            return a & b
    elif name == 'or':
        def __call__(self, a: int, b: int) -> int:
            return a | b
    elif name == 'xor':
        def __call__(self, a: int, b: int) -> int:
            return a ^ b
