import pickle
import pkg_resources

# List of 2Q gates
two_qubit_gates = ['cx',  'cy',   'cz',  'ch',   'dcx', 
		   'csx', 'csdg', 'ecr', 'swap', 'iswap']

def load_pauli_twirling_dict():
    """Return a dataframe with Pauli Twirling sets for common
       two-qubit Clifford Gates.
    """
    stream = pkg_resources.resource_stream(__name__, 'data/twirling_sets.pkl')
    return pickle.load(stream)

def load_cxgate_twirls():
    return load_pauli_twirling_dict()['cx']

def load_cygate_twirls():
    return load_pauli_twirling_dict()['cy']

def load_czgate_twirls():
    return load_pauli_twirling_dict()['cz']

def load_chgate_twirls():
    return load_pauli_twirling_dict()['ch']

def load_dcxgate_twirls():
    return load_pauli_twirling_dict()['dcx']

def load_csxgate_twirls():
    return load_pauli_twirling_dict()['csx']

def load_csdggate_twirls():
    return load_pauli_twirling_dict()['csdg']

def load_ecrgate_twirls():
    return load_pauli_twirling_dict()['ecr']

def load_swapgate_twirls():
    return load_pauli_twirling_dict()['swap']

def load_iswapgate_twirls():
    return load_pauli_twirling_dict()['iswap']





"""
def get_pauli_twirling_dict(gate="", include_phase=True):
    if not gate:
        dictionary = pickle.load(data/twirling_sets.pkl)
    elif gate not in two_qubit_gates:
        print('Not a valid gate name. Valid gate names are:\n')
        print('cx, cy, cz, ch, dcx, csx, csdg, ecr, swap, iswap\n')
    else:
        temp_dict = pickle.load(data/twirling_sets.pkl)
        dictionary = temp_dict['cx']
    return dictionary
"""
