from Visualizations.Binary.BinaryWire import BinaryWire


def connect_layers(upper_layer: list, lower_layer: list) -> list:
    canvas = upper_layer[0].canvas
    wire_pairs = []
    for gate_node in lower_layer:
        node_0, node_1 = upper_layer[gate_node.gate.indices[0]], upper_layer[gate_node.gate.indices[1]]
        wire_pairs.append((BinaryWire(canvas=canvas, start_node=node_0, end_node=gate_node),
                           BinaryWire(canvas=canvas, start_node=node_1, end_node=gate_node)))
    return wire_pairs
