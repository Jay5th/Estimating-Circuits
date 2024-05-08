from Visualizations.Binary.BinaryNode import BinaryNode
from BooleanCircuits.CircuitConstruction.BinaryGate import BinaryGate
import tkinter as tk


def create_gate_layer(canvas: tk.Canvas, binary_gates: list, x: int, y: int, node_radius: int) -> list:
    layer_size = len(binary_gates)
    center_points_range = 3 * node_radius * (layer_size - 1)
    left_center_x = x - center_points_range // 2
    gate_layer = []
    for i in range(layer_size):
        xi = left_center_x + 3 * node_radius * i
        gate_layer.append(BinaryNode(canvas=canvas, gate=binary_gates[i], x=xi, y=y, radius=node_radius))
    return gate_layer
