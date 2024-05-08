from Visualizations.Binary.BinaryNode import BinaryNode
from BooleanCircuits.CircuitConstruction.BinaryGate import BinaryGate
import tkinter as tk


def create_gate_layer(canvas: tk.Canvas, operation_indices_pairs: list, x: int, y: int, radius: int) -> list:
    layer_size = len(operation_indices_pairs)
    center_points_range = 3 * radius * (layer_size - 1)
    left_center_x = x - center_points_range // 2
    gate_layer = []
    for i in range(layer_size):
        xi = left_center_x + 3 * radius * i
        operation, indices = operation_indices_pairs[i]
        gate_layer.append(BinaryNode(canvas=canvas, gate=BinaryGate(indices=indices, operation=operation),
                                     x=xi, y=y, radius=radius))
    return gate_layer
