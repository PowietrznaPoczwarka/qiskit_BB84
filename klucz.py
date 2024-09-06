from qiskit import QuantumCircuit, execute, Aer
from numpy.random import randint
import numpy as np
import os

from qiskit_BB84.alice import alice_nadaje, alice_klucz
#from eve import eve_odbiera
from qiskit_BB84.bob import bob_odbiera, bob_klucz

num_qubits = 64
circuit = QuantumCircuit(num_qubits)

circ = alice_nadaje(circuit, num_qubits)
#circ = eve_odbiera(circ, num_qubits)
circ = bob_odbiera(circ, num_qubits)

# Po nadaniu kubitów przez Alice i odebraniu oraz zmierzeniu przez Boba spotykają się i dzielą się swoimi bramkami H
alice_basis = os.environ.get('BAZY ALICE')
bob_basis = os.environ.get('BAZY BOB')

print(f"Bazy, których użyła Alice:\t {alice_basis}")
print(f"Bazy, których użył Bob:\t\t {bob_basis} \n")

# Po wymianie stanów bramek H, Bob i Alice konstruują swoje klucze i sprawdzają je, wykorzystując do tego ich pierwsze 8 znaków - reszta posłuży za rzeczywisty klucz
alice_state = os.environ.get('STAN ALICE')
alice_key_check = alice_klucz(alice_state, alice_basis, bob_basis)

bob_state = os.environ.get('STAN BOB')
bob_key_check = bob_klucz(bob_state, alice_basis, bob_basis)

if alice_key_check == bob_key_check:
    print("Nikt nie podsłuchiwał. Klucz jest bezpieczny")
else:
    print("Ktoś podłuchiwał - połączenie nie jest bezpieczne")