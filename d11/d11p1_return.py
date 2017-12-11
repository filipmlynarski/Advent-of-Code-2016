import sys
import time
import pprint
from copy import deepcopy

puzzle = open('puzzle').read().splitlines()

structures = [[]]
for idx, i in enumerate(puzzle):
	this = i.split(' ')
	structures[0].append([])
	for j in range(len(this)):
		if this[j].startswith('microchip'):
			structures[0][idx].append(this[j - 1][0].upper() + 'M')
		elif this[j].startswith('generator'):
			structures[0][idx].append(this[j - 1][0].upper() + 'G')
	structures[0][idx] = sorted(structures[0][idx])

structures[0][0] = ['E'] + structures[0][0]
structures2 = []
checked = []

def fine(floor):
	for generator in [i for i in floor if i[-1] == 'G']:
		if not (generator[0] + 'M' in floor):
			for chip in [i for i in floor if i[-1] == 'M']:
				if not (chip[0] + 'G' in floor):
					return False
	return True

def do(x, away, to, a, b):
	x2 = deepcopy(x)
	x2[away] = a
	x2[to] = b
	if len(x2[0]) == 0 and len(x2[1]) == 0 and len(x2[2]) == 0:
		global done
		done = True
	return x2

def one(x, away, to):
	ret = []

	for chip in [things for things in x[away] if things[-1] == 'M']:
		test1 = sorted(x[to] + [chip] + ['E'])
		test2 = sorted([i for i in x[away] if i != chip and i != 'E'])
		if fine(test1) and fine(test2):
			save = do(x, away, to, test2, test1)
			if not save in checked:
				checked.append(save)
				ret.append(save)

		for rest in [things for things in x[away] if things != 'E' and things != chip]:
			test1 = sorted(x[to] + [rest] + [chip] + ['E'])
			test2 = sorted([i for i in x[away] if i != chip and i != rest and i != 'E'])
			if fine(test1) and fine(test2):
				save = do(x, away, to, test2, test1)
				if not save in checked:
					checked.append(save)
					ret.append(save)

	return ret

def move(blue):
	for high, floors in enumerate(blue):
		if 'E' in floors:
			if high == 0:
				return one(blue, high, high + 1)
			elif high == 1 or high == 2:
				return one(blue, high, high + 1) + one(blue, high, high - 1)
			elif high == 3:
				return one(blue, high, high - 1)

steps = 0
done = False
while not done and steps < 15:
	steps += 1
	print len(checked)
	for structure in structures:
		save1 = move(structure)
		structures2.extend(save1)

	structures = deepcopy(structures2)
	structures2 = []
print steps