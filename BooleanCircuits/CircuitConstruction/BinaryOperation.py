from dataclasses import dataclass

available_options = {'zero': lambda a, b: 0,
                     'one': lambda a, b: 1,
                     'and': lambda a, b: a & b,
                     'or': lambda a, b: a | b,
                     'xor': lambda a, b: a ^ b}


@dataclass(frozen=True)
class BinaryOperation:
    name: str = 'zero'

    def __call__(self, a: int, b: int) -> int:
        return available_options[self.name](a, b)
