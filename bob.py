from qiskit import QuantumCircuit, execute, Aer
from numpy.random import randint
import numpy as np
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.providers.aer import QasmSimulator
import os

def bob_odbiera(circuit, num_qubits):
    """Bob odbiera układ kubitów, stosuje swoją bazę bramek H i mierzy kubity w celu otrzymania stanu końcowego"""
    bob_basis = np.random.randint(2, size=num_qubits)
    
    for i in range(len(bob_basis)): # dla kazdego bitu w bazie odbiorcy (pozycje bramek H)
        if bob_basis[i] == 1:
            circuit.h(i)

    circuit.measure_all()

    key = execute(circuit.reverse_bits(),backend=QasmSimulator(),shots=1).result().get_counts().most_frequent()
    
    os.environ['BAZY BOB'] = "".join(bob_basis.astype(str))
    os.environ['STAN BOB'] = key
    
    return circuit

def bob_klucz(key, alice_basis, bob_basis):
    """Bob na podstawie baz swoich i Alice ze zmierzonego stanu kubitów tworzy pełny klucz"""
    bob_encryption_key = ''
    for i in range(len(bob_basis)):
        if alice_basis[i] == bob_basis[i]:
            bob_encryption_key += str(key[i])
    print(f"Klucz Boba (8 pierwszych znaków): \t {bob_encryption_key[0:8]}")
    bob_key_check = bob_encryption_key[0:8]
    os.environ['KLUCZ BOB'] = bob_encryption_key[8::]
    
    return bob_key_check