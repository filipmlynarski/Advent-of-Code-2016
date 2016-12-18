puzle = open('puzzle')
puzzle = []
import sys
def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret
for i in puzle:
	puzzle.append(i.split('\n')[0])
def change(x):
	ret = ')'.join((x.split(')')[1:]))[: int(x.split(')')[0].split('x')[0].split('(')[1])] * int(x.split(')')[0].split('x')[1])
	idx = len(x.split(')')[0]) + 1 + len(')'.join((x.split(')')[1:]))[: int(x.split(')')[0].split('x')[0].split('(')[1])])
	return ret + x[idx:]
def count(x):
	wynik = 0
	for idx, i in enumerate(x):
		if i == '(':
			return wynik + count(change(x[idx:]))
		else:
			wynik += 1
	return wynik
i = join(puzzle)
sys.setrecursionlimit(1000000)
print count(i)