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


## Dependancies
---


## Function Documentation
---
`get_pauli_twirling_dict(gate="", IncludePhase=True)`
- Gate must be one of the following gates (links to Qiskit documentation):
  - [CXGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CXGate.html)
  - [CYGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CYGate.html)
  - [CZGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CZGate.html)
  - [CHGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CHGate.html)
  - [DCXGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.DCXGate.html)
  - [CSXGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CSXGate.html)
  - [CSdgGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CSdgGate.html)
  - [ECRGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.ECRGate.html)
  - [SWAPGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.SwapGate.html)
  - [iSWAPGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.iSwapGate.html)
- There isn't support for including/not including the phase yet; it's included no matter what is passed to `IncludePhase`.

`generate_pauli_twirling_sets(TwoQubitGate())`
- The `TwoQubitGate()` should to be a two-qubit instance of the Qiskit [Gate](https://qiskit.org/documentation/stubs/qiskit.circuit.Gate.html) class.
- Finds Pauli Twirls for the given Gate; returns a structure of the form: `[(gates,phase), (gates,phase), ...)]`.

`CLASS PauliTwirling(PassManager)`
-  Bases: `PassManager` ([PassManager Class in Qiskit](https://qiskit.org/documentation/stubs/qiskit.transpiler.PassManager.html))


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
Import the `PauliTwirling` class:
```python
from quantum_twirling.pauli_twirling import PauliTwirling
```
Create a two-qubit quantum circuit to Pauli Twirl.
Note that the two-qubit gate in this circuit is a CX gate. 
Thus, we can use our `cx_dict` retrieved from `get_pauli_twirling_dict('cx')`, earlier.
```python
qc = QuantumCircuit(3)
qc.h(1)
qc.cx(1,0)
qc.cx(1,2)
qc.draw('mpl')
```
To use the pass, attach to a `PassManager`. 
Here, we do that and tell our `PauliTwirling` pass to twirl CX gates in our `cx_dict`.
```python
pm = PassManager([PauliTwirling('cx_dict', seed=54321)])
twirl_qc = pm.run(qc)
twirl_qc.draw('mpl')
```
Call `pm.run` once and draw the circuit:
```python
twirl_qc = pm.run(qc)
twirl_qc.draw('mpl')
```
Subsequent calls will yield other circuits that are likewise randomly twirled.


## Acknowledgements
---
[IBM Quantum: Generating Pauli-twirled circuits in Qiskit](https://quantum-enablement.org/posts/2023/2023-02-02-pauli_twirling.html)



