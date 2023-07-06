#################################################
###  Program:      generate_dict.py           ###
###  Date Created: July 05, 2023              ###
###  Author:       Lydia England              ###
###  Contact:      lydiajoyengland@gmail.com  ###
###                (253) 549-5000             ###
#################################################

import numpy as np
from itertools import combinations
import pickle
# import json

# from qiskit import qpy

from qiskit import *
# Need gate classes for generating the Pauli twirling sets
from qiskit.circuit.library import (IGate,   XGate,   YGate,   ZGate,
                                    CXGate,  CYGate,    CZGate,  CHGate,
                                    CSGate,  DCXGate,   CSXGate, CSdgGate, 
                                    RXXGate, RYYGate,   RZZGate, RZXGate,  
                                    ECRGate, iSwapGate, SwapGate)

# Operator class
from qiskit.quantum_info import Operator

# Classes for building up a directed-acyclic graph (DAG) structure
from qiskit.circuit import QuantumRegister
from qiskit.dagcircuit import DAGCircuit
# Transpiler stuff neded to make a pass and passmanager
from qiskit.transpiler import PassManager
from qiskit.transpiler.basepasses import TransformationPass
from qiskit.transpiler.passes import Optimize1qGatesDecomposition

# A fake system to transpile against
# from qiskit.providers.fake_provider import FakeHanoiV2



######################
###  DECLARATIONS  ###
######################

# Single qubit Pauli gates
I = IGate()    # identity 
Z = ZGate()    # pauli Z 
X = XGate()    # pauli X
Y = YGate()    # pauli Y

# 2Q entangling gates
CX    = CXGate()     # cnot; controlled-X
CY    = CYGate()     # controlled-Y
CZ    = CZGate()     # controlled-Z
CH    = CHGate()     # controlled-Hadamard
CS    = CSGate()     # controlled-S
DCX   = DCXGate()    # double cnot 
CSX   = CSXGate()    # controlled sqrt X
CSdg  = CSdgGate()   # controlled S^dagger
ECR   = ECRGate()    # echoed cross-resonance 
Swap  = SwapGate()   # swap
iSwap = iSwapGate()  # imaginary swap
# RXX   = RXXGate()    # parametric 2-qubit X \otimes X interaction (rot. abt XX)
# RYY   = RYYGate()    # parametric 2-qubit Y \otimes Y interaction (rot. abt YY)
# RZZ   = RZZGate()    # parametric 2-qubit Z \otimes Z interaction (rot. abt ZZ)
# RZX   = RZXGate()    # parametric 2-qubit Z \otimes X interaction (rot. abt ZX)


# List of 2Q gates
# two_qubit_gates = [CX, CY, CZ, CH, CS, DCX, CSX, CSdg, 
#                    ECR, Swap, iSwap, RXX, RYY, RZZ, RZX]
two_qubit_gates = [CX, CY, CZ, CH, CS, DCX, CSX, CSdg, 
                   ECR, Swap, iSwap]



##########################
###  DEFINE FUNCTIONS  ###
##########################

"""Find all possible combinations of Paulis that leave the action 
    of a two-qubit gate unchanged, up to a phase factor.
    Treat as a 16 choose 4 problem, and let Python generate all the 
    possibilities.
    If the unitary remains unchanged, then we add the combination 
    of Paulis to the output list, along with a phase value of Zero.
    However, if the unitaries differ by a phase factor of pi, 
    we add a global phase of pi.
"""

def generate_pauli_twirling_sets(two_qubit_gate):
    """Generate the Pauli twirling sets for a given 2Q gate
    
    Sets are ordered such that gate[0] and gate[1] are pre-rotations
    applied to control and target, respectively.  gate[2] and gate[3]
    are post-rotations for control and target, respectively.
    
    Parameters:
        two_qubit_gate (Gate): Input two-qubit gate
        
    Returns:
        list: List of all twirling gate sets
    """
    # Generate 16 element list of Pauli gates, each repeated 4 times
    operator_list = [I, Z, X, Y]*4
    # This is the target unitary to which our twirled circuit should match
    target_unitary = Operator(two_qubit_gate.to_matrix())
    twirling_sets = []
    
    # For every combination in 16 choose 4 make a circuit and look for equivilence
    for gates in combinations(operator_list, 4):
        # Build a circuit for our twirled 2Q gate
        qc = QuantumCircuit(2)
        qc.append(gates[0], [0])
        qc.append(gates[1], [1])
        qc.append(two_qubit_gate, [0, 1])
        qc.append(gates[2], [0])
        qc.append(gates[3], [1])
        
        norm = np.linalg.norm(Operator.from_circuit(qc)-target_unitary)
        
        phase = None
        # If unitaries match we have a phase of zero
        if abs(norm) < 1e-15:
            phase = 0
        # If unitaries differ by a phase of pi, shift by pi
        elif abs(norm-4) < 1e-15:
            phase = np.pi

        if phase is not None:
            qc.global_phase += phase
            # Verify that our twirled circuit is a valid replacement
            assert Operator.from_circuit(qc) == target_unitary
            twirl_set = (gates, phase)
            # Check that set does not already exist
            if twirl_set not in twirling_sets:
                twirling_sets.append(twirl_set)
            
    return twirling_sets




###################
###  EXECUTION  ###
###################

"""Generate the sets for each of the two-qubit gate instances above.
    Store the sets in a dictionary with the gate name as the key. 
"""

twirling_groups = {}

for gate in two_qubit_gates:
    twirl_set = generate_pauli_twirling_sets(gate)
    twirling_groups[gate.name] = twirl_set

# Write the dictionary to a .txt file
with open('twirling_groups.pkl', 'wb') as fd:
    pickle.dump(twirling_groups, fd)















