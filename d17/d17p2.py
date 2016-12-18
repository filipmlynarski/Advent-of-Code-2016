puzle = open('puzzle')
puzzle = []

def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret
for i in puzle:
	puzzle.append(i.split('\n')[0])