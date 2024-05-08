from Visualizations.Binary.InputNode import InputNode
import tkinter as tk


def create_input_layer(canvas: tk.Canvas, input_size: int, x: int, y: int, radius: int) -> list:
    center_points_range = 3 * radius * (input_size - 1)
    left_center_x = x - center_points_range // 2
    input_nodes = []
    for i in range(input_size):
        xi = left_center_x + 3 * radius * i
        input_nodes.append(InputNode(canvas=canvas, input_index=i, x=xi, y=y, radius=radius))
    return input_nodes
