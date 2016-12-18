from copy import deepcopy

puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret

puzzle = join(puzzle)

def reverse(x):
	ret = ''
	for idx, i in enumerate(x):
		ret += x[len(x) - (idx + 1)]
	return ret
def change(x):
	ret = ''
	for i in x:
		if i == '1':
			ret += '0'
		else:
			ret += '1'
	return ret
def curve(x):
	a = x
	b = a
	b = reverse(b)
	b = change(b)
	return a + '0' + b
def checksum(x):
	ret = ''
	for idx in range(len(x)):
		if idx % 2 == 0 or idx == 0:
			if x[idx] == x[idx + 1]:
				ret += '1'
			else:
				ret += '0'
	return ret

while len(puzzle) < 35651584:
	puzzle = curve(puzzle)

puzzle = puzzle[:35651584]
puzzle = checksum(puzzle)

while len(puzzle) % 2 == 0:
	puzzle = checksum(puzzle)
print puzzle