from copy import deepcopy
import numpy as np
puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

def swap(x, idx, swaper):
	ret = ''
	for idx2, i in enumerate(x):
		if idx2 == idx:
			ret += swaper
		else:
			ret += i
	return ret

def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret
