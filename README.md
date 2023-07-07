# Quantum-Twirling
A Python package designed for fast implementation of [Pauli Twirling](/#What-Is-Pauli-Twirling?) in [Qiskit](https://qiskit.org/documentation/) circuits.


## Features
--- 
- It includes a fast built-in dictionary of Pauli Twirling Sets for Qiskit two-qubit Clifford gates CX, CY, CZ, CH, DCX, CSX, CSdg, ECR, SWAP, iSWAP.
- It can generate Pauli Twirling Sets for any given two-qubit gate.
- If used with an instance of Qiskit's PassManager, it can implement randomized Pauli Twirls to a circuit containing two-qubit gates.


## Contents
---
- [Features](/#Features)
- [What is Pauli Twirling?](/#What-is-Pauli-Twirling?)
  - [Implementation of Pauli Twirling in Academic Literature](#/Implementation-of-Pauli-Twirling)
- [Function Documentation](/#Function-Documentation)
- [Usage and Examples](/#Usage-and-Examples)
  - [Load](/#Load-Pauli-Twirling-Sets)
  - [Generate](/#Generate-Pauli-Twirling-Sets)
  - [Twirl Qiskit Circuits](/#Twirl-Qiskit-Circuits)
- [Acknowledgements](/#Acknowledgements)


## What is Pauli Twirling?
---
**Pauli Twirling** is a powerful error supression/mitigation technique for quantum circuits.
By combining the results from many random, yet logically equivalent circuits, it converts an arbitrary noise channel into a *stochastic* Pauli error channel, thus suppressing off-diagonal coherent error contributions. 
It is implemented by sandwiching a two-qubit Clifford gate between randomly sampled single-qubit twirling gates drawn from a set of Pauli operations.

Crucially, the gates are selected such that the net operation, in the absence of noise, is unchanged.
That is, the Pauli Twirling Set for a two-qubit Clifford gate is a set of four Pauli gates that when pre-pended and appended to a circuit containing the two-qubit gate, the unitary is equal to that of the single two-qubit gate alone.

### Implementation of Pauli Twirling in Academic Literature
---
- [Purification of noisy entanglement and faithful teleportation via noisy channels (Bennet, et. al., 1996)](https://arxiv.org/abs/quant-ph/9511027)
- [Mixed state entanglement and quantum error correction (Bennet, et. al., 1996)](https://arxiv.org/abs/quant-ph/9604024)
- [Practical Implementations of Twirl Operations (Anwar, Short, and Jones, 2008)](https://arxiv.org/pdf/quant-ph/0409142.pdf)
- [Scalable error mitigation for noisy quantum circuites produces competitive expectation values (Kim, et. al., 2021)](https://www.nature.com/articles/s41567-022-01914-3)
- [Constructing smaller Pauli twirling sets for arbitrary error channels (Cai and Benjamin, 2018)](https://arxiv.org/abs/1807.04973v3)


## Dictionary-Supported Qiskit Gates 
Native Pauli Twirling Sets are included for the following common two-qubit Clifford gates in Qiskit: 
- [CXGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CXGate.html) (Controlled X Gate, a.k.a. CNOT Gate)
- [CYGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CYGate.html) (Controlled Y Gate)
- [CZGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CZGate.html) (Controlled Z Gate)
- [CHGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CHGate.html) (Controlled Hadamard Gate)
- [DCXGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.DCXGate.html) (Double Controlled X Gate, a.k.a., Double CNOT Gate)
- [CSXGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CSXGate.html) (Controlled Square Root of X Gate)
- [CSdgGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.CSdgGate.html) (Controlled S^dagger Gate)
- [ECRGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.ECRGate.html) (Echoed Cross-Resonance Gate)
- [SWAPGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.SwapGate.html) (Swap Gate)
- [iSWAPGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.iSwapGate.html) (Imaginary Swap Gate)


## Documentation
---

### Module: `load_pauli_twirling_sets`

Import Module:
```python
from quantum_twirling import load_pauli_twirling_sets
```
---
Load the entire Pauli Twirling Sets dictionary:
```python
quantum_twirling.load_pauli_twirling_sets.load_pauli_twirling_dict()
```
Output is the full dictionary. 
Each gate's Pauli Twirling Sets can be accessed by passing the lowercase name of the gate to the dictionary, 
e.g: `cx_twirls = pauli_twirling_dict['cx']` 

---
Return list of CX Gate Pauli Twirling Sets:
```python
quantum_twirling.load_pauli_twirling_sets.load_cxgate_twirls()
```
---
Return list of CY Gate Pauli Twirling Sets:
```python
quantum_twirling.load_pauli_twirling_sets.load_cygate_twirls()
```
---
Return list of CZ Gate Pauli Twirling Sets:
```python
quantum_twirling.load_pauli_twirling_sets.load_czgate_twirls()
```
---
Return list of CH Gate Pauli Twirling Sets:
```python
quantum_twirling.load_pauli_twirling_sets.load_chgate_twirls()
```
---
Return list of DCX Gate Pauli Twirling Sets:
```python
quantum_twirling.load_pauli_twirling_sets.load_dcxgate_twirls()
```
---
Return list of CSX Gate Pauli Twirling Sets:
```python
quantum_twirling.load_pauli_twirling_sets.load_csxgate_twirls()
```
---
Return list of CSdg Gate Pauli Twirling Sets:
```python
load_pauli_twirling_sets.load_csdggate_twirls()
```
---
Return list of ECR Gate Pauli Twirling Sets:
```python
load_pauli_twirling_sets.load_ecrgate_twirls()
```
---
Return list of SWAP Gate Pauli Twirling Sets:
```python
load_pauli_twirling_sets.load_swapgate_twirls()
```
---
Return list of iSWAP Gate Pauli Twirling Sets:
```python
load_pauli_twirling_sets.load_iswapgate_twirls()
```


### Module: generate_pauli_twirling_sets
---
Import Module:
```python
from quantum_twirling import generate_pauli_twirling_sets
```
---
```python
generate_pauli_twirling_sets(TwoQubitGate())
```
- The `TwoQubitGate()` should to be a two-qubit instance of the Qiskit [Gate](https://qiskit.org/documentation/stubs/qiskit.circuit.Gate.html) class.
- Finds Pauli Twirls for the given Gate; returns a list of the form: `[(gates,phase), (gates,phase), ...)]`.


### Module: pauli_twirling
---
Import Module:
```python
from quantum_twirling import pauli_twirling
```
---
```python
CLASS PauliTwirling(PassManager)
```
-  Bases: `PassManager` ([PassManager Class in Qiskit](https://qiskit.org/documentation/stubs/qiskit.transpiler.PassManager.html))
To twirl all instances of a given two-qubit gate in a quantum circuit, attach `PauliTwirling` pass to a Qiskit `PassManager`.
Tell the `PauliTwirling` pass to twirl gates of a certain type by providing a list of Pauli Twirling Sets for a given two-qubit gate.
Seed the pass; Pauli Twirls are randomly applied to circuit.
```python
pm = PassManager([PauliTwirling(gate_twirling_sets, seed=" ")])
```
To use the pass, call `pm.run(qc)` where `qc` is a quantum circuit. 
All gates of type given in `PassManager` will be randomly Pauli Twirled.
Subsequent calls of `pm.run(qc)` will yield other circuits that are likewise randomly twirled.




## Usage and Examples
---

```python
import qiskit
import quantum_twirling
from quantum_twirling import load_pauli_twirling_sets
from quantum_twirling.generate_pauli_twirling_sets import generate_pauli_twirling_sets
from quantum_twirling.pauli_twirling import PauliTwirling
```

### Load Pauli Twirling Sets
Load the entire existing dictionary with `load_pauli_twirling_dict()`:
```python
twirl_dict = load_pauli_twirling_sets.load_pauli_twirling_dict()
```
Load individual gate twirling sets with: `cxgate_twirls()`, etc:
```python
cx_twirls = load_pauli_twirling_sets.load_cxgate_twirls()
cy_twirls = load_pauli_twirling_sets.load_cygate_twirls()
cz_twirls = load_pauli_twirling_sets.load_czgate_twirls()
ch_twirls = load_pauli_twirling_sets.load_chgate_twirls()
dcx_twirls = load_pauli_twirling_sets.load_dcxgate_twirls()
csx_twirls = load_pauli_twirling_sets.load_csxgate_twirls()
csdg_twirls = load_pauli_twirling_sets.load_csdggate_twirls()
ecr_twirls = load_pauli_twirling_sets.load_ecrgate_twirls()
swap_twirls = load_pauli_twirling_sets.load_swapgate_twirls()
iswap_twirls = load_pauli_twirling_sets.load_iswapgate_twirls()
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



