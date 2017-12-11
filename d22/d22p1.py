from copy import deepcopy
puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])
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
		if i[0] == x:
			return [True, i]
	return [False]
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
def space(x):
	ret = []
	for i in x:
		if i != '':
			ret.append(i)
	return ret
puzzle = puzzle[2:]
nodes = []
pairs = 0

for i in puzzle:
	nodes.append(space(i.split(' ')))
	if int(space(i.split(' '))[2][:-1]) < 31:
		print i
for i in nodes:
	beg = '/dev/grid/node-x'
	x = i[0].split('-')[1].split('x')[1]
	y = i[0].split('-')[2].split('y')[1]

	if check(beg + str(int(x) + 1) + '-y' + y, nodes)[0]:
		i2 = check(beg + str(int(x) + 1) + '-y' + y, nodes)[1]
		#print int(i[2][:-1])
		if i[2][0] != '0' and int(i[2][:-1]) <= int(i2[3][:-1]):
			print i
			print i2
			print int(i[2][:-1])
			pairs += 1
			#pairs.append(i[2][0])

	if check(beg + str(int(x) - 1) + '-y' + y, nodes)[0]:
		i2 = check(beg + str(int(x) - 1) + '-y' + y, nodes)[1]
		if i[2][0] != '0' and int(i[2][:-1]) <= int(i2[3][:-1]):
			print i
			print i2
			print int(i[2][:-1])
			pairs += 1
			#pairs.append(i[2][0])

	if check(beg + x + '-y' + str(int(y) + 1), nodes)[0]:
		i2 = check(beg + x + '-y' + str(int(y) + 1), nodes)[1]
		if i[2][0] != '0' and int(i[2][:-1]) <= int(i2[3][:-1]):
			print i
			print i2
			print int(i[2][:-1])
			pairs += 1
			#pairs.append(i[2][0])

	if check(beg + x + '-y' + str(int(y) - 1), nodes)[0]:
		i2 = check(beg + x + '-y' + str(int(y) - 1), nodes)[1]
		if i[2][0] != '0' and int(i[2][:-1]) <= int(i2[3][:-1]):
			print i
			print i2
			print int(i[2][:-1])
			pairs += 1
			#pairs.append(i[2][0])
print pairs