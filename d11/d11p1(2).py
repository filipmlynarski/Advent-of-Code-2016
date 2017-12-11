from copy import deepcopy
import numpy as np
puzle = open('puzzle')
puzzle = []
def amount(x):
	ret = [1,[]]
	for i in x:
		for idx, j in enumerate(i.split(' ')):
			if j.startswith('generator'):
				ret[1].append(i.split(' ')[idx - 1][0].upper() + 'G')
				ret[0] += 1
			elif j.startswith('microchip'):
				ret[1].append(i.split(' ')[idx - 1].split('-')[0][0].upper() + 'M')
				ret[0] += 1
	return ret
def less(x):
	ret = []
	for i in x:
		count = 0
		for j in i:
			if j == '1':
				count += 1
		if count < 3:
			ret.append(i)
	return ret
def idx_of(x, y):
	for idx, i in enumerate(y):
		if x == i:
			return idx
def check(y, x):
	for i in y:
		if i == x:
			return True
	return False
def dec_to_bin(x):
    return int(bin(x)[2:])
def combs(x):
	ret = []
	elevator = 0
	save_idxs = []
	for idx, i in enumerate(x):
		if i[1] == 'E':
			save = i[0]
			elevator = idx
			for idx2, j in enumerate(i):
				if j[0] != 'F' and j != 'E' and j != '.':
					save_idxs.append(idx2 - 2)

	for i in range(2 ** len(save_idxs)):
		ret.append((len(save_idxs) - len(str(dec_to_bin(i)))) * '0' + str(dec_to_bin(i)))

	real_ret = ['' for i in range(len(ret))]
	for i in range(amount(puzzle)[0]):
		for idx, j in enumerate(ret):
			if not check(save_idxs, i):
				real_ret[idx] += '0'
			else:
				real_ret[idx] += j[idx_of(i, save_idxs)]
	return rem0ve(less(real_ret[1:])), save


for i in puzle:
	puzzle.append(i.split('\n')[0])

floors = [['F' + str(i + 1)] + amount(puzzle)[0] * ['.'] for i in range(4)]
point = 1
floors[0][1] = 'E'
for idx_i, i in enumerate(puzzle):
	for idx, j in enumerate(i.split(' ')):
		if j.startswith('generator'):
			point += 1
			floors[idx_i][point] = i.split(' ')[idx - 1][0].upper() + 'G'
		elif j.startswith('microchip'):
			point += 1
			floors[idx_i][point] = i.split(' ')[idx - 1].split('-')[0][0].upper() + 'M'
def rem0ve(x):
	ret = []
	for i in range(len(x)):
		dont = False
		for j in range(i + 1, len(x)):
			if x[i] == x[j]:
				dont = True
		if not dont:
			ret.append(x[i])
	return ret
def change(x, skad, dokad, co):
	ret = deepcopy(x)

	for idx2, j in enumerate(co):
		if j == '1':
			ret[int(dokad[1]) - 1][idx2 + 2] = x[int(skad[1]) - 1][idx2 + 2]
			ret[int(skad[1]) - 1][idx2 + 2] = '.'
			ret[int(dokad[1]) - 1][1] = 'E'
			ret[int(skad[1]) - 1][1] = '.'
	return ret

def good(x):
	for i in x:
		if len(i) > 1 and i[1] == 'M':
			if not check(x, i[0] + 'G'):
				for j in x:
					if len(j) > 1 and j[1] == 'G':
						return False
	return True

def possible(x):
	for i in x:
		#if i[1] == 'E':
		if not good(i):
			return False
	return True
floorses = [floors]
end = False
finall_count = 0
def done(x):
	for i in x:
		if i == '.':
			return False
	return True

while not end:
	finall_count += 1
	floorses2 = []
	for i in floorses:
		komba = combs(i)
		for j in komba[0]:
			if komba[1] == 'F1':
				higher = change(i, komba[1], 'F' + str(int(komba[1][1]) + 1), j)
				if possible(higher):
					floorses2.append(higher)
			elif komba[1] == 'F4':
				lower = change(i, komba[1], 'F' + str(int(komba[1][1]) - 1), j)
				if possible(lower):
					floorses2.append(lower)
			else:
				higher = change(i, komba[1], 'F' + str(int(komba[1][1]) + 1), j)
				if possible(higher):
					if done(higher[3][1:]):
						print finall_count
						end = True
					floorses2.append(higher)
				lower = change(i, komba[1], 'F' + str(int(komba[1][1]) - 1), j)
				if possible(lower):
					floorses2.append(lower)
	floorses = deepcopy(rem0ve(floorses2))
	print 'count =',finall_count
	print 'len floorses2 =',len(floorses2)
