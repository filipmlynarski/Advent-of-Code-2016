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
def check(y, x):
	for i in y:
		if i == x:
			return True
	return False
def dec_to_bin(x):
    return int(bin(x)[2:])

floors = [['F' + str(i + 1), '.', '.', '.', '.', '.'] for i in range(4)]
floors[0][1] = 'E'

for idx, i in enumerate(puzzle):
	for j in i.split(' '):
		if j == 'hydrogen-compatible':
			floors[idx][3] = 'HM'
		elif j == 'lithium-compatible':
			floors[idx][5] = 'LM'
		elif j == 'hydrogen':
			floors[idx][2] = 'HG'
		elif j == 'lithium':
			floors[idx][4] = 'LG'
floorses = [floors]
end = True
def idx_of(x, y):
	for idx, i in enumerate(y):
		if x == i:
			return idx
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
	for i in range(4):
		for idx, j in enumerate(ret):
			if not check(save_idxs, i):
				real_ret[idx] += '0'
			else:
				real_ret[idx] += j[idx_of(i, save_idxs)]
	return less(real_ret[1:]), save
def change(x, skad, dokad, co):
	ret = deepcopy(x)

	for idx2, j in enumerate(co):
		if j == '1':
			ret[int(dokad[1]) - 1][idx2 + 2] = x[int(skad[1]) - 1][idx2 + 2]
			ret[int(skad[1]) - 1][idx2 + 2] = '.'
			ret[int(dokad[1]) - 1][1] = 'E'
			ret[int(skad[1]) - 1][1] = '.'

	return ret
def possible(x):
	for i in x:
		if (i[2] == 'HG' and i[3] == '.' and i[4] == '.' and i[5] == 'LM') or (i[2] == '.' and i[3] == 'HM' and i[4] == 'LG' and i[5] == '.'):
			return False
	return True
file = open('test')
test = []
for i in file:
	test.append(i.split('\n')[0])
def remove_space(x):
	ret = []
	for i in x:
		ret.append([])
		for j in i.split(' '):
			if j != '':
				ret[len(ret) - 1].append(j)
	return ret
test = remove_space(test)
#print possible(test)

final_count = 0
while end:
	final_count += 1
	floorses2 = []
	for i in floorses:
		for j in combs(i)[0]:
			if combs(i)[1] == 'F1':
				higher = change(i, combs(i)[1], 'F' + str(int(combs(i)[1][1]) + 1), j)
				if possible(higher):
					floorses2.append(higher)
			elif combs(i)[1] == 'F4':
				lower = change(i, combs(i)[1], 'F' + str(int(combs(i)[1][1]) - 1), j)
				if possible(lower):
					floorses2.append(lower)
			else:
				higher = change(i, combs(i)[1], 'F' + str(int(combs(i)[1][1]) + 1), j)
				if possible(higher):
					floorses2.append(higher)
				lower = change(i, combs(i)[1], 'F' + str(int(combs(i)[1][1]) - 1), j)
				if possible(lower):
					floorses2.append(lower)
	floorses = deepcopy(floorses2)
	print final_count
	print len(floorses)
	for i in floorses:
		if i[3][2] != '.' and i[3][3] != '.' and i[3][4] != '.' and i[3][5] != '.':
			print final_count
			end = False
