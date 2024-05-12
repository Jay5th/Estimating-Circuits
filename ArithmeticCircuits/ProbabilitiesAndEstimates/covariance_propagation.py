from ArithmeticCircuits.CircuitConstruction.ArithmeticCircuit import ArithmeticCircuit


def ordered_gates_parent_locations(circuit: ArithmeticCircuit) -> dict:
    parent_locations = {}
    previous_layer_start = 0
    current_index = len(circuit.gate_layers[0])
    for i in range(1, len(circuit.gate_layers)):
        current_layer = circuit.gate_layers[i]
        for gate in current_layer:
            parent_locations[current_index] = (previous_layer_start + gate.indices[0],
                                               previous_layer_start + gate.indices[1])
            current_index += 1
        previous_layer_start += len(circuit.gate_layers[i-1])
    return parent_locations


def covariance_propagation(circuit: ArithmeticCircuit) -> float:
    mu = {}
    sigma = {}
    ordered_gates = [gate for layer in circuit.gate_layers for gate in layer]
    parent_locations = ordered_gates_parent_locations(circuit)
    for k in range(len(ordered_gates)):
        gate = ordered_gates[k]
        gate_op = gate.operation
        if gate_op.name not in ('sum', 'product'):
            mu[k] = gate_op(0, 0)
            if gate_op.name != 'first':  # constant case
                for j in range(k + 1):
                    sigma[(j, k)] = 0
            else:  # input case
                sigma[(k, k)] = 1
                for j in range(k):
                    sigma[(j, k)] = 0
        else:
            ak, bk = parent_locations[k]
            ak_bk = tuple(sorted([ak, bk]))
            if gate_op.name == 'sum':  # sum case
                mu[k] = mu[ak] + mu[bk]
                sigma[(k, k)] = sigma[(ak, ak)] + 2 * sigma[ak_bk] + sigma[(bk, bk)]
                for j in range(k):
                    j_ak = tuple(sorted([j, ak]))
                    j_bk = tuple(sorted([j, bk]))
                    sigma[(j, k)] = sigma[j_ak] + sigma[j_bk]
            else:  # product case
                mu[k] = mu[ak] * mu[bk] + sigma[(ak, bk)]
                sigma[(k, k)] = (sigma[ak_bk]**2 + 2*sigma[ak_bk]*mu[ak]*mu[bk] + sigma[(ak, ak)]*sigma[(bk, bk)]
                                 + sigma[(ak, ak)]*mu[bk]**2 + sigma[(bk, bk)]*mu[ak]**2)
                for j in range(k):
                    j_ak = tuple(sorted([j, ak]))
                    j_bk = tuple(sorted([j, bk]))
                    sigma[(j, k)] = sigma[j_ak]*mu[bk] + sigma[j_bk]*mu[ak]
    return mu[len(ordered_gates)-1]
