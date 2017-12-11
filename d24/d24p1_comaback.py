import sys
from copy import deepcopy

puzzle = open('puzzle').read().splitlines()

points = {}

for line_idx, line in enumerate(puzzle):
	for mark_idx, mark in enumerate(line):
		if mark.isdigit():
			points[mark] = [line_idx, mark_idx]

connections = {}
for idx, i in enumerate(points):
	for j in range(idx + 1, len(points)):
		connections[str(idx) + str(j)] = 'NaN'
def rem0ve(x):
	ret = []
	for i in range(len(x)):
		dont = False
		for j in range(i + 1, len(x)):
			if x[i][-1] == x[j][-1]:
				dont = True
		if not dont:
			ret.append(x[i])
	return ret
def find(x):
	print 'liczymy: ' + x
	paths  = [[points[x[0]]]]
	paths2 = []
	iterator = 0
	while True:
		iterator += 1
		for i in paths:

			t = i + [[i[-1][0] + 1, i[-1][1]]]
			if puzzle[t[-1][0]][t[-1][1]] == x[1]:
				return iterator
			elif puzzle[t[-1][0]][t[-1][1]] != '#' and (len(t) < 3 or t[-1] != t[-3]):
				paths2.append(t)

			t = i + [[i[-1][0], i[-1][1] + 1]]
			if puzzle[t[-1][0]][t[-1][1]] == x[1]:
				return iterator
			elif puzzle[t[-1][0]][t[-1][1]] != '#' and (len(t) < 3 or t[-1] != t[-3]):
				paths2.append(t)

			t = i + [[i[-1][0] - 1, i[-1][1]]]
			if puzzle[t[-1][0]][t[-1][1]] == x[1]:
				return iterator
			elif puzzle[t[-1][0]][t[-1][1]] != '#' and (len(t) < 3 or t[-1] != t[-3]):
				paths2.append(t)

			t = i + [[i[-1][0], i[-1][1] - 1]]
			if puzzle[t[-1][0]][t[-1][1]] == x[1]:
				return iterator
			elif puzzle[t[-1][0]][t[-1][1]] != '#' and (len(t) < 3 or t[-1] != t[-3]):
				paths2.append(t)

		paths = deepcopy(rem0ve(paths2))
		paths2 = []

def dupli(x):
	for i in range(len(x)):
		for j in range(i + 1, len(x)):
			if x[i] == x[j]:
				return True
	return False
def path(x):
	ret = 0
	for i in range(len(x) - 1):
		ret += connections[x[i] + x[i+1]]
	return ret


for i in sorted(connections):
	length = find(i)
	connections[i] = length
	connections[i[1] + i[0]] = length

i = int(''.join([str(nmbr) for nmbr in range(1, len(points))]))
allowed = str(''.join([str(nmbr) for nmbr in range(1, len(points))]))
current = 9999999999999999999
while int(i) < int(''.join([str(nmbr) for nmbr in reversed(range(1, len(points)))])):
	if not dupli('0' + str(i)) and all(map(lambda j: j in allowed, str(i))):
		if path(str('0' + str(i))) < current:
			current = path(str('0' + str(i)))
	i += 1

print current

'''
liczymy: 01
01: 78
liczymy: 02
02: 206
liczymy: 03
03: 198
liczymy: 04
04: 208
liczymy: 05
05: 246
liczymy: 06
06: 56
liczymy: 07
07: 62
liczymy: 12
12: 268
liczymy: 13
13: 260
liczymy: 14
14: 270
liczymy: 15
15: 308
liczymy: 16
16: 94
liczymy: 17
17: 32
liczymy: 23
23: 4
8liczymy: 24
24: 38
liczymy: 25
25: 52
liczymy: 26
26: 190
liczymy: 27
27: 240
liczymy: 34
34: 66
liczymy: 35
35: 84
liczymy: 36
36: 182
liczymy: 37
37: 232
liczymy: 45
45: 58
liczymy: 46
46: 192
liczymy: 47
47: 242
liczymy: 56
56: 230
liczymy: 57
57: 280
liczymy: 67
67: 66
wynik: 502
'''