import pickle

# List of 2Q gates
two_qubit_gates = ['cx',  'cy',   'cz',  'ch',   'dcx', 
		   'csx', 'csdg', 'ecr', 'swap', 'iswap']

def get_pauli_twirling_dict(gate="", include_phase=True):
    if not gate:
        dictionary = pickle.load(data/twirling_sets.pkl)
    elif gate not in two_qubit_gates:
	print('Not a valid gate name.\nValid gate names are:\n
		cx, cy, cz, ch, dcx, csx, csdg, ecr, swap, iswap\n')
    else:
        temp_dict = pickle.load(data/twirling_sets.pkl)
        dictionary = temp_dict['cx']
    return dictionary 
