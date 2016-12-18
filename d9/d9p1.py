puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])
def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret
def sice(x, idx):
	for i in range(idx, len(x)):
		if x[i] == ')':
			return x[idx + 1:i]
i = join(puzzle)
new = ''
freeze = 0
for idx, j in enumerate(i):
	if freeze <= idx and j == '(':
		new += i[len(sice(i, idx)) + 2 + idx : len(sice(i, idx)) + 2 + idx + int(sice(i, idx).split('x')[0])] * int(sice(i, idx).split('x')[1])
		freeze = len(sice(i, idx)) + 2 + idx + int(sice(i, idx).split('x')[0])

	elif freeze <= idx:
		new += j

print len(new)