import tkinter as tk
from BooleanCircuits.CircuitConstruction.BinaryGate import BinaryGate


class BinaryNode:
    def __init__(self, canvas: tk.Canvas, gate: BinaryGate, x: int, y: int, radius: int, color_off: str = 'gray',
                 color_on: str = 'aqua'):
        self.canvas = canvas
        self.gate = gate
        self.node_id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color_off)
        self.text_id = canvas.create_text(x, y, text=gate.operation.name.upper())
        self.center = x, y
        self.radius = radius
        self.colors = color_off, color_on
        self.output = gate.operation(0, 0)

    def place(self, x: int, y: int):
        dx, dy = x - self.center[0], y - self.center[1]
        self.canvas.move(self.node_id, dx, dy)
        self.canvas.move(self.text_id, dx, dy)
        self.center = x, y

    def activate(self, data_input: tuple):
        self.output = self.gate(data_input)
        self.canvas.itemconfigure(self.node_id, fill=self.colors[self.output])
        return self.output

    def deactivate(self):
        self.output = self.gate.operation(0, 0)
        self.canvas.itemconfigure(self.node_id, fill=self.colors[self.output])

    def get_output(self):
        return self.output
