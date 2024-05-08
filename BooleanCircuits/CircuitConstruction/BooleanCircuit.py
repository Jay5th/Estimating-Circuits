from dataclasses import dataclass


@dataclass
class BooleanCircuit:
    input_size: int
    gate_layers: list

    def pass_through_layer(self, data_input: tuple, layer_index: int) -> tuple:
        layer = self.gate_layers[layer_index]
        return tuple([gate(data_input) for gate in layer])

    # Forward pass
    def __call__(self, data_input: tuple) -> tuple or int:
        data_stream = tuple(data_input)
        for layer_index in range(len(self.gate_layers)):
            data_stream = self.pass_through_layer(data_stream, layer_index)
        if len(data_stream) == 1:
            data_stream = data_stream[0]
        return data_stream
