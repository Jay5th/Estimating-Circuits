import tkinter as tk
from Visualizations.Binary.create_input_layer import create_input_layer
from Visualizations.Binary.create_gate_layer import create_gate_layer
from Visualizations.HelperFunctions.connect_layers import connect_layers
from BooleanCircuits.CircuitConstruction.BinaryOperation import BinaryOperation

root = tk.Tk()

root.geometry("700x700")
canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()

or_op = BinaryOperation('or')
and_op = BinaryOperation('and')
xor_op = BinaryOperation('xor')


input_layer = create_input_layer(canvas=canvas, input_size=3, x=300, y=50, radius=30)
layer_1 = create_gate_layer(canvas=canvas, operation_indices_pairs=[(or_op, (0, 1)), (xor_op, (0, 2)), (or_op, (1, 2))],
                            x=300, y=150, radius=30)
connect_layers(input_layer, layer_1)
layer_2 = create_gate_layer(canvas=canvas, operation_indices_pairs=[(and_op, (0, 1)), (and_op, (1, 2))],
                            x=300, y=250, radius=30)
connect_layers(layer_1, layer_2)
layer_3 = create_gate_layer(canvas=canvas, operation_indices_pairs=[(xor_op, (0, 1))],
                            x=300, y=350, radius=30)
connect_layers(layer_2, layer_3)


root.mainloop()
