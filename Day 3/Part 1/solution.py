import numpy as np
from scipy import stats

with open('input.txt') as f:
	inp = np.array([list(x) for x in f.read().splitlines()])
	gamma = stats.mode(inp, axis=0).mode.flatten()
	epsilon = (gamma == np.array(['0']*len(gamma))).astype(int).astype(str)
	gamma = int(''.join(gamma), 2)
	epsilon = int(''.join(epsilon), 2)
	print(gamma*epsilon)