import numpy as np
puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])
time = -1
found = False
puzzle.append('Disc #7 has 11 positions; at time=0, it is at position 0.')
while not found:
	time += 1
	time2 = time
	found = True
	for i in puzzle:
		time2 += 1
		if not ((int(i.split(' ')[11][:-1]) + time2) % int(i.split(' ')[3]) == 0 and found):
			found = False

print time