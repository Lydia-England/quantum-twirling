#################################################
###  Program:      pauli_twirling.py          ###
###  Date Created: July 07, 2023              ###
###  Author:       Lydia England              ###
###  Contact:      lydiajoyengland@gmail.com  ###
###                (253) 549-5000             ###
#################################################

import numpy as np   
from itertools import combinations
import pickle
from qiskit import *
# Need gate classes for generating the Pauli twirling sets
from qiskit.circuit.library import (IGate,   XGate,   YGate,   ZGate,
                                    CXGate,  CYGate,    CZGate,  CHGate,
                                    CSGate,  DCXGate,   CSXGate, CSdgGate, 
                                    ECRGate, iSwapGate, SwapGate)
# Operator class
from qiskit.quantum_info import Operator
# Classes for building up a directed-acyclic graph (DAG) structure
from qiskit.circuit import QuantumRegister
from qiskit.dagcircuit import DAGCircuit
# Transpiler stuff neded to make a pass and passmanager
# from qiskit.transpiler import PassManager
from qiskit.transpiler.basepasses import TransformationPass
# from qiskit.transpiler.passes import Optimize1qGatesDecomposition



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

# List of 2Q gates
two_qubit_gates = [CX, CY, CZ, CH, CS, DCX, 
                   CSX, CSdg, ECR, Swap, iSwap]


# with open('twirling_groups.pkl', 'rb') as f:
#    twirling_groups = pickle.load(f)


##################################
###  Twirling Qiskit Circuits  ###
##################################

"""Class called pauli_twirling that performs twirling on a specific
    two-qubit gate, and utilizes the dictionary of twirling sets generated above.
"""

class PauliTwirling(TransformationPass):
    """Pauli twirl an input circuit.
    """
    def __init__(self, twirling_gate, seed=None):
        """
        Parameters:
            twirling_gate (str): Which gate to twirl
            seed (int): Seed for RNG, should be < 2e32
        """
        super().__init__()
        # This is the target gate to twirl
        self.twirling_gate = twirling_gate
        # Get the twirling set from the dict we generated above
        # This should be repalced by a cached version in practice
        self.twirling_set = twirling_groups[twirling_gate]
        # Length of the twirling set to bound RNG generation
        self.twirling_len = len(self.twirling_set)
        # Seed the NumPy RNG
        self.rng = np.random.default_rng(seed)

    def run(self, dag):
        """Insert Pauli twirls into input DAG
        
        Parameters:
            dag (DAGCircuit): Input DAG
        
        Returns:
            dag: DAG with twirls added in-place
        """
        for run in dag.collect_runs([self.twirling_gate]):
            for node in run:
                # Generate a random int to specify the twirling gates
                twirl_idx = self.rng.integers(0, self.twirling_len)
                # Get the randomly selected twirling set
                twirl_gates = self.twirling_set[twirl_idx][0]
                twirl_phase = self.twirling_set[twirl_idx][1]
                # Make a small DAG for the twirled circuit we are going to insert
                twirl_dag = DAGCircuit()
                # Add a register of qubits (here always 2Q)
                qreg = QuantumRegister(2)
                twirl_dag.add_qreg(qreg)
                # gate[0] pre-applied to control
                twirl_dag.apply_operation_back(twirl_gates[0], [qreg[0]])
                # gate[1] pre-applied to target
                twirl_dag.apply_operation_back(twirl_gates[1], [qreg[1]])
                # Insert original gate
                twirl_dag.apply_operation_back(node.op, [qreg[0], qreg[1]])
                # gate[2] pre-applied to control
                twirl_dag.apply_operation_back(twirl_gates[2], [qreg[0]])
                # gate[3] pre-applied to target
                twirl_dag.apply_operation_back(twirl_gates[3], [qreg[1]])
                # Add a global phase gate to account for possible phase difference
                twirl_dag.global_phase += twirl_phase
                # Replace the target gate with the twirled version
                dag.substitute_node_with_dag(node, twirl_dag)
        return dag















