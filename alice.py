from qiskit import QuantumCircuit
from numpy.random import randint
import numpy as np
import os

def alice_nadaje(circuit, num_qubits):
    """Alice generuje losowy klucz oraz swoje bazy i przekazuje kubity dalej (docelowo do Boba)"""
    alice_state = np.random.randint(2, size=num_qubits) #klucz generowany i wysylany
    alice_basis = np.random.randint(2, size=num_qubits) #Alice generuje też bazy
    
    for i in range(len(alice_basis)): #dla kazdego bitu w bazie nadawcy (pozycje bramek H)
        if alice_state[i] == 1: 
            circuit.x(i)
        if alice_basis[i] == 1:
            circuit.h(i)
    
    os.environ['BAZY ALICE'] = "".join(alice_basis.astype(str))
    os.environ['STAN ALICE'] = "".join(alice_state.astype(str))
    
    return circuit

def alice_klucz(alice_state, alice_basis, bob_basis):
    """Alice na podstawie baz swoich i Boba z losowo wygenerowanego stanu tworzy pełny klucz"""
    alice_encryption_key = ''
    for i in range(len(alice_basis)):
        if alice_basis[i] == bob_basis[i]:
            alice_encryption_key += str(alice_state[i])
    print(f"Klucz Alice (8 pierwszych znaków): \t {alice_encryption_key[0:8]}")
    alice_key_check = alice_encryption_key[0:8]
    
    os.environ['KLUCZ ALICE'] = alice_encryption_key[8::]
    
    return alice_key_check