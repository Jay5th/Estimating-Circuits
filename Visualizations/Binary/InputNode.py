import tkinter as tk


class InputNode:
    def __init__(self, canvas: tk.Canvas, input_index: int, x: int, y: int, radius: int, color_off: str = 'gray',
                 color_on: str = 'aqua'):
        self.canvas = canvas
        self.input_index = input_index
        self.node_id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color_off)
        self.text_id = canvas.create_text(x, y, text="z"+str(input_index+1))
        self.center = x, y
        self.radius = radius
        self.colors = color_off, color_on
        self.output = 0

    def place(self, x: int, y: int):
        dx, dy = x - self.center[0], y - self.center[1]
        self.canvas.move(self.node_id, dx, dy)
        self.canvas.move(self.text_id, dx, dy)
        self.center = x, y

    def activate(self, data_input: tuple):
        self.output = data_input[self.input_index]
        self.canvas.itemconfigure(self.node_id, fill=self.colors[self.output])
        return self.output

    def deactivate(self):
        self.output = 0
        self.canvas.itemconfigure(self.node_id, fill=self.colors[0])

    def get_output(self):
        return self.output
