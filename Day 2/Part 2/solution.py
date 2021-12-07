import numpy as np

with open('input.txt') as f:
	x = 0
	y = 0
	aim = 0

	for line in f.readlines():
		command, units = line.rstrip('\n').split()
		units = int(units)

		if command == 'forward':
			x += units
			y += aim * units
		if command == 'down':
			aim += units
		if command == 'up':
			aim -= units

	print(y*x)