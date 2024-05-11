from dataclasses import dataclass
from ArithmeticCircuits.CircuitConstruction.ArithmeticGate import ArithmeticGate


@dataclass
class ArithmeticCircuit:
    gate_layers: list[list[ArithmeticGate]]

    def pass_through_layer(self, data_input: tuple[float, ...], layer_index: int) -> tuple[float, ...]:
        layer = self.gate_layers[layer_index]
        return tuple([gate(data_input) for gate in layer])

    # Forward pass
    def __call__(self, data_input: tuple[float, ...]) -> tuple[float, ...] or float:
        data_stream = tuple(data_input)
        for layer_index in range(len(self.gate_layers)):
            data_stream = self.pass_through_layer(data_stream, layer_index)
        if len(data_stream) == 1:
            data_stream = data_stream[0]
        return data_stream
