import numpy as np

with open('input.txt') as f:
	depths = np.array(f.readlines())
	depths = [int(x.rstrip('\n')) for x in depths]
	depths = np.convolve(depths, np.ones(3), 'valid')
	print((np.diff(depths) > 0).sum())