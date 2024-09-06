from qiskit import QuantumCircuit, execute, Aer
from numpy.random import randint
import numpy as np
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.providers.aer import QasmSimulator
import os

def eve_odbiera(circuit, num_qubits):
    """Eve podsłuchuje i odbiera układ kubitów, stosuje swoją bazę bramek H, mierzy kubity i wysyła je potem do Boba"""
    # Eve nie wie jeszcze jaki układ bramek H stosuje Alice, ponieważ Alice dzieli się tym z Bobem dopiero potem
    # Musi więc stworzyć swój układ bramek H
    eve_basis = np.random.randint(2, size=num_qubits)
    
    for i in range(len(eve_basis)): # dla kazdego bitu w bazie odbiorcy (pozycje bramek H)
        if eve_basis[i] == 1:
            circuit.h(i)

    circuit.measure_all()
    key = execute(circuit.reverse_bits(),backend=QasmSimulator(),shots=1).result().get_counts().most_frequent()
    print(f"Pełny klucz, który podsłuchała Eve to:\t {key} \n")
    
    # Eve musi ponownie zakodować układ kubitów i wysłać go do Boba, aby ten niczego nie podejrzewał.
    
    for i in range(len(eve_basis)): # dla kazdego bitu w bazie odbiorcy (pozycje bramek H)
        if eve_basis[i] == 1:
            circuit.h(i)
    
    return circuit
