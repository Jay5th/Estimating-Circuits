import tkinter as tk
from Visualizations.Binary.BinaryNode import BinaryNode
from Visualizations.Binary.InputNode import InputNode
from Visualizations.HelperFunctions.normalized_vector import normalized_vector


class BinaryWire:
    def __init__(self, canvas: tk.Canvas, start_node: BinaryNode or InputNode, end_node: BinaryNode,
                 color_off: str = 'black', color_on: str = 'aqua'):
        self.canvas = canvas
        self.start_node = start_node
        self.end_node = end_node
        self.data_flow = start_node.get_output()
        self.colors = (color_off, color_on)
        x0, y0 = start_node.center
        x1, y1 = end_node.center
        forward_direction = normalized_vector((x1-x0, y1-y0))
        backward_direction = normalized_vector((x0-x1, y0-y1))
        wire_start_x = int(x0 + start_node.radius * forward_direction[0])
        wire_start_y = int(y0 + start_node.radius * forward_direction[1])
        wire_end_x = int(x1 + end_node.radius * backward_direction[0])
        wire_end_y = int(y1 + end_node.radius * backward_direction[1])
        self.id = canvas.create_line(wire_start_x, wire_start_y, wire_end_x, wire_end_y, arrow='last',
                                     fill=self.colors[self.data_flow], width=2)

    def update(self):
        self.data_flow = self.start_node.get_output()
        self.canvas.itemconfigure(self.id, fill=self.colors[self.data_flow])

    def get_data_flow(self):
        return self.data_flow
