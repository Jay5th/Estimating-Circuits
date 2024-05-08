import tkinter as tk
import time
from BooleanCircuits.CircuitConstruction.BooleanCircuit import BooleanCircuit
from Visualizations.Binary.create_input_layer import create_input_layer
from Visualizations.Binary.create_gate_layer import create_gate_layer
from Visualizations.Binary.connect_layers import connect_layers


class BinaryNetwork:
    def __init__(self, canvas: tk.Canvas, circuit: BooleanCircuit, node_radius: int, wire_length: int):
        canvas.master.update()
        center_x = canvas.winfo_width() // 2
        center_y = canvas.winfo_height() // 2
        layer_count = len(circuit.gate_layers) + 1
        network_height = (2 * node_radius + wire_length) * (layer_count - 1) + 2 * node_radius
        top_layer_y = center_y - (network_height - 2 * node_radius) // 2
        self.canvas = canvas
        self.network_layers = [create_input_layer(canvas=canvas, input_size=circuit.input_size, x=center_x,
                                                  y=top_layer_y, node_radius=node_radius)]
        self.wire_pair_layers = []
        for i in range(layer_count-1):
            layer_y = top_layer_y + (i + 1) * (2 * node_radius + wire_length)
            self.network_layers.append(create_gate_layer(canvas=canvas, binary_gates=circuit.gate_layers[i],
                                                         x=center_x, y=layer_y, node_radius=node_radius))
            self.wire_pair_layers.append(connect_layers(upper_layer=self.network_layers[i],
                                                        lower_layer=self.network_layers[i+1]))

    def pass_through_layer(self, data_input: tuple, layer_index: int, delay: int or float = 0) -> tuple or int:
        output = []
        node_layer = self.network_layers[layer_index]
        for i in range(len(node_layer)):
            output.append(node_layer[i].activate(data_input))
        if len(self.wire_pair_layers) > layer_index:
            self.canvas.update()
            time.sleep(delay)
            for wires in self.wire_pair_layers[layer_index]:
                wires[0].update()
                wires[1].update()
        if len(output) == 1:
            output = output[0]
        else:
            output = tuple(output)
        return output

    def __call__(self, data_input: tuple, delay: int or float = 0) -> tuple or int:
        data_stream = tuple(data_input)
        for i in range(len(self.network_layers)):
            data_stream = self.pass_through_layer(data_input=data_stream, layer_index=i, delay=delay)
        return data_stream

    def reset(self):
        for i in range(len(self.network_layers)):
            layer = self.network_layers[i]
            for j in range(len(layer)):
                layer[j].deactivate()
            if len(self.wire_pair_layers) > i:
                for wires in self.wire_pair_layers[i]:
                    wires[0].update()
                    wires[1].update()
