
from copy import deepcopy
puzle = open('puzzle')
puzzle = []
def swap(x, y, z):
	new = ''
	for idx, i in enumerate(x):
		if idx != y and idx != z:
			new += i
		elif idx == y:
			new += x[z]
		else:
			new += x[y]
	return new
def swap2(x, y, z):
	new = ''
	for i in x:
		if i != y and i != z:
			new += i
		elif i == y:
			new += z
		else:
			new += y
	return new
def idx_of(x, y):
	for idx, i in enumerate(x):
		if i == y:
			return idx
def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret
def check(x, y):
	for i in y:
		if i == x:
			return True
	return False
def is_int(x):
	nmbrs = '0,1,2,3,4,5,6,7,8,9'.split(',')
	for i in nmbrs:
		if i == x:
			return True
	return False
def reverse(x):
	ret = ''
	for i in range(len(x)):
		ret += x[len(x) - (i + 1)]
	return ret
def reverse_array(x):
	ret = []
	for i in range(len(x)):
		ret.append(x[len(x) - (i + 1)])
	return ret
def last(x, y ,z):
	new = ''
	for idx, i in enumerate(x):
		if idx != int(y):
			if int(y) > int(z):
				if idx == int(z):
					new += x[int(y)]
				new += i
			else:
				new += i
				if idx == int(z):
					new += x[int(y)]
	return new
def maybe(x):
	ret = []
	for idx, i in enumerate(x):
		ret.append(x[idx:] + x[: idx])
	return ret
tekst = 'fbgdceah'

idxs = [i + 1 for i in range(len(tekst))]
for idx, i in enumerate(idxs):
	if i >= 4:
		idxs[idx] += 1
	idxs[idx] %= len(tekst)
for i in puzle:
	puzzle.append(i.split('\n')[0])
puzzle = reverse_array(puzzle)

for index, i in enumerate(puzzle):
	if i.split(' ')[0] == 'swap':
		if is_int(i.split(' ')[2]):
			tekst = swap(tekst, int(i.split(' ')[2]), int(i.split(' ')[5]))
		else:
			tekst = swap2(tekst, i.split(' ')[2], i.split(' ')[5])
	elif i.split(' ')[0] == 'reverse':
		tekst = tekst[: int(i.split(' ')[2])] + reverse(tekst[int(i.split(' ')[2]): int(i.split(' ')[4]) + 1]) + tekst[int(i.split(' ')[4]) + 1: ]
	elif i.split(' ')[0] == 'rotate':
		if i.split(' ')[1] == 'right':
			tekst = tekst[int(i.split(' ')[2]) :] + tekst[: int(i.split(' ')[2])]
		elif i.split(' ')[1] == 'left':
			tekst = tekst[-int(i.split(' ')[2]) :] + tekst[: -int(i.split(' ')[2])]
		else:
			tekst_save = maybe(tekst)
			for tryes in tekst_save:
				idx = idx_of(tryes, i.split(' ')[6]) + 1
				if idx_of(tryes, i.split(' ')[6]) >= 4:
					idx += 1
				idx %= len(tekst)
				if tryes[-idx :] + tryes[: -idx] == tekst:
					tekst = tryes
					break

	else:
		if int(i.split(' ')[5]) < int(i.split(' ')[2]):
			tekst = last(tekst, i.split(' ')[5], int(i.split(' ')[2]))
		else:
			tekst = last(tekst, i.split(' ')[5], int(i.split(' ')[2]))
print tekst