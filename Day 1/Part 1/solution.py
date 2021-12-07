import numpy as np

with open('input.txt') as f:
	depths = np.array(f.readlines())
	depths = [int(x.rstrip('\n')) for x in depths]
	print((np.diff(depths) > 0).sum())