import tkinter as tk
from BooleanCircuits.CircuitConstruction.BinaryOperation import BinaryOperation
from BooleanCircuits.CircuitConstruction.random_circuit import random_circuit
from Visualizations.Binary.BinaryNetwork import BinaryNetwork

or_op = BinaryOperation(name='or')
and_op = BinaryOperation(name='and')
xor_op = BinaryOperation(name='xor')
binary_ops = [BinaryOperation(name='or'), BinaryOperation(name='and'), BinaryOperation(name='xor')]

root = tk.Tk()
root.geometry("700x700")

canvas = tk.Canvas(root, width=600, height=600, bg='bisque1')
canvas.pack()

circuit = random_circuit(input_size=5, binary_operations=binary_ops, max_layer_size=5)
network = BinaryNetwork(canvas=canvas, circuit=circuit, node_radius=40, wire_length=20)

# Data input
input_label = tk.Label(root, text="Data Input:")
input_label.place(x=250, y=625)

input_entry = tk.Entry(root, width=25)
input_entry.place(x=250, y=650)

# Delay input
delay_label = tk.Label(root, text="Update delay (sec):")
delay_label.place(x=25, y=625)

delay_entry = tk.Entry(root, width=25)
delay_entry.place(x=25, y=650)

# Activate button


def activate_command():
    data_input = eval(input_entry.get())
    delay = eval(delay_entry.get())
    network(data_input=data_input, delay=delay)


activate_button = tk.Button(root, text="Activate", command=activate_command)
activate_button.place(x=500, y=625)


# Reset button


def reset_command():
    network.reset()


reset_button = tk.Button(root, text="Reset", command=reset_command)
reset_button.place(x=500, y=655)


root.mainloop()
