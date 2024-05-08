from dataclasses import dataclass

available_options = {'zero': lambda a, b: 0,
                     'one': lambda a, b: 1,
                     'and': lambda a, b: a & b,
                     'or': lambda a, b: a | b,
                     'xor': lambda a, b: a ^ b}


@dataclass(frozen=True)
class BinaryOperation:
    name: str = 'zero'
    assert name in available_options.keys(), f"I have not implemented a binary operation named {name}."

    def __call__(self, a: int, b: int) -> int:
        return available_options[self.name](a, b)
