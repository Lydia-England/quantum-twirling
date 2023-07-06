# Quantum-Twirling
A Python package designed for fast implementation of [Pauli Twirling](/##What-Is-Pauli-Twirling?) in [Qiskit](https://qiskit.org/documentation/) circuits.




## Features
--- 
- It includes a fast built-in dictionary of Pauli Twirling Sets for Qiskit two-qubit Clifford gates CX, CY, CZ, CH, DCX, CSX, CSdg, ECR, SWAP, iSWAP.
- It can generate Pauli Twirling Sets for any given two-qubit gate.
- If used with an instance of Qiskit's PassManager, it can implement randomized Pauli Twirls to a circuit containing two-qubit gates.


## Contents
---
- [Features](/##Features)
- [What is Pauli Twirling?](/##What-is-Pauli-Twirling?)
- [Usage and Examples](/##Usage-and-Examples)
- [Acknowledgements](/##Acknowledgements)



## What is Pauli Twirling?
---
**Pauli Twirling** is a powerful error supression/mitigation technique for quantum circuits.
By combining the results from many random, yet logically equivalent circuits, it converts an arbitrary noise channel into a *stochastic* Pauli error channel, thus suppressing off-diagonal coherent error contributions. 
It is implemented by sandwiching a two-qubit Clifford gate between randomly sampled single-qubit twirling gates drawn from a set of Pauli operations.

Crucially, the gates are selected such that the net operation, in the absence of noise, is unchanged.
That is, the Pauli Twirling Set for a two-qubit Clifford gate is a set of four Pauli gates that when pre-pended and appended to a circuit containing the two-qubit gate, the unitary is equal to that of the single two-qubit gate alone.

### Implementation of Pauli Twirling
---
- [Purification of noisy entanglement and faithful teleportation via noisy channels (Bennet, et. al., 1996)](https://arxiv.org/abs/quant-ph/9511027)
- [Mixed state entanglement and quantum error correction (Bennet, et. al., 1996)](https://arxiv.org/abs/quant-ph/9604024)
- [Practical Implementations of Twirl Operations (Anwar, Short, and Jones, 2008)](https://arxiv.org/pdf/quant-ph/0409142.pdf)
- [Scalable error mitigation for noisy quantum circuites produces competitive expectation values (Kim, et. al., 2021)](https://www.nature.com/articles/s41567-022-01914-3)
- [Constructing smaller Pauli twirling sets for arbitrary error channels (Cai and Benjamin, 2018)](https://arxiv.org/abs/1807.04973v3)



## Usage and Examples
---
```python
import quantum_twirling
```

### Load Pauli Twirling Sets
```python
from quantum_twirling import load_pauli_twirling_sets
cx_dict = get_pauli_twirling_dict('cx')
```

### Generate Pauli Twirling Sets
```python
from quantum_twirling import generate_pauli_twirling_sets
twirling_sets = generate_pauli_twirling_sets(TwoQubitGate)
```

### Twirl Qiskit Circuits
```python
from quantum_twirling.pauli_twirling import PauliTwirling
pm = PassManager([PauliTwirling('cx', seed=54321)])
twirl_qc = pm.run(quantum_circuit)
twirl_qc.draw('mpl')
```


## Acknowledgements
---
[IBM Quantum: Generating Pauli-twirled circuits in Qiskit](https://quantum-enablement.org/posts/2023/2023-02-02-pauli_twirling.html)



