import numpy as np

with open('input.txt') as f:
	x = 0
	y = 0
	for line in f.readlines():
		command, units = line.rstrip('\n').split()
		units = int(units)

		if command == 'forward':
			x += units
		if command == 'down':
			y += units
		if command == 'up':
			y -= units
	print(y*x)