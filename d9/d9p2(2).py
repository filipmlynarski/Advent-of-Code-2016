puzle = open('puzzle')
puzzle = []

def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret
for i in puzle:
	puzzle.append(i.split('\n')[0])
def nawias(x):
	for i in x:
		if i == '(':
			return True
	return False
puzzle = join(puzzle)
def gimme(x, idx):
	ret = ''
	for idx2, i in enumerate(x):
		ret += x[idx + idx2]
		if x[idx + idx2] == ')':
			return ret
def how_far(x):
	for idx, i in enumerate(x):
		if i == '(':
			ilosc = len(gimme(x, idx)) + int(x.split(')')[0].split('(')[len(x.split(')')[0].split('(')) - 1].split('x')[0]) + idx
			break
	for idx, i in enumerate(x):
		if i == '(' and idx != 0 and idx < ilosc:
			gimi = gimme(x, idx)
			if ilosc < len(gimi) + idx + int(gimi.split('x')[0][1:]):
				ilosc = len(gimi) + idx + int(gimi.split('x')[0][1:])
	return x[:int(ilosc)]


def count(x):
	ret = 0
	while nawias(x):
		for i in x:
			if i == '(':
				razy = x.split(')')[0].split('(')[len(x.split(')')[0].split('(')) - 1].split('x')[1]
				ilosc = x.split(')')[0].split('(')[len(x.split(')')[0].split('(')) - 1].split('x')[0]
				ret += int(razy) * count(x[len(gimme(x, 0)):len(how_far(x))])
				x = x[len(how_far(x)):]
				break
			else:
				ret += 1
				x = x[1:]
	return ret + len(x)

wynik = 0

while nawias(puzzle):
	for i in puzzle:
		if i == '(':
			wynik += int(gimme(puzzle, 0).split('x')[1][:-1]) * count(puzzle[len(gimme(puzzle, 0)):len(how_far(puzzle))])
			puzzle = puzzle[len(how_far(puzzle)):]
			break
		else:
			wynik += 1
			puzzle = puzzle[1:]

print wynik + len(puzzle)