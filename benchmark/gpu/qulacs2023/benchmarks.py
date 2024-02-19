import numpy as np
from qulacs2023 import Circuit, QuantumState, RX, RZ, CNOT

import pytest

nqubits_list = range(4, 26)

def first_rotation(circuit, nqubits):
    for k in range(nqubits):
        circuit.add_gate(RX(k, np.random.rand()))
        circuit.add_gate(RZ(k, np.random.rand()))


def mid_rotation(circuit, nqubits):
    for k in range(nqubits):
        circuit.add_gate(RZ(k, np.random.rand()))
        circuit.add_gate(RX(k, np.random.rand()))
        circuit.add_gate(RZ(k, np.random.rand()))


def last_rotation(circuit, nqubits):
    for k in range(nqubits):
        circuit.add_gate(RZ(k, np.random.rand()))
        circuit.add_gate(RX(k, np.random.rand()))


def entangler(circuit, nqubits, pairs):
    for a, b in pairs:
        circuit.add_gate(CNOT(a, b))


def build_circuit(nqubits, depth, pairs):
    circuit = Circuit(nqubits)
    first_rotation(circuit, nqubits)
    entangler(circuit, nqubits, pairs)
    for k in range(depth):
        mid_rotation(circuit, nqubits)
        entangler(circuit, nqubits, pairs)

    last_rotation(circuit, nqubits)
    return circuit


def benchfunc_noopt(circuit, nqubits):
    st = QuantumState(nqubits)
    circuit.update_quantum_state(st)


@pytest.mark.parametrize('nqubits', nqubits_list)
def test_QCBM(benchmark, nqubits):
    benchmark.group = "QCBM"
    pairs = [(i, (i + 1) % nqubits) for i in range(nqubits)]
    circuit = build_circuit(nqubits, 9, pairs)
    benchmark(benchfunc_noopt, circuit, nqubits)
