import tkinter as tk
from BooleanCircuits.CircuitConstruction.BooleanCircuit import BooleanCircuit
from BooleanCircuits.CircuitConstruction.BinaryGate import BinaryGate
from BooleanCircuits.CircuitConstruction.BinaryOperation import BinaryOperation
from Visualizations.Binary.BinaryNetwork import BinaryNetwork


root = tk.Tk()

root.geometry("700x700")


canvas = tk.Canvas(root, width=600, height=600, bg='bisque1')
canvas.pack()

or_op = BinaryOperation(name='or')
and_op = BinaryOperation(name='and')
xor_op = BinaryOperation(name='xor')

gate_layers = []

layer0 = [BinaryGate(indices=(0, 1), operation=or_op),
          BinaryGate(indices=(0, 2), operation=xor_op),
          BinaryGate(indices=(1, 2), operation=or_op)]
gate_layers.append(layer0)

layer1 = [BinaryGate(indices=(0, 1), operation=and_op),
          BinaryGate(indices=(1, 2), operation=and_op)]
gate_layers.append(layer1)

layer2 = [BinaryGate(indices=(0, 1), operation=xor_op)]
gate_layers.append(layer2)

simple_boolean_circuit = BooleanCircuit(input_size=3, gate_layers=gate_layers)

simple_network = BinaryNetwork(canvas=canvas, circuit=simple_boolean_circuit, node_radius=40, wire_length=20)

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
    simple_network(data_input=data_input, delay=delay)


activate_button = tk.Button(root, text="Activate", command=activate_command)
activate_button.place(x=500, y=625)


# Reset button


def reset_command():
    simple_network.reset()


reset_button = tk.Button(root, text="Reset", command=reset_command)
reset_button.place(x=500, y=655)


root.mainloop()
