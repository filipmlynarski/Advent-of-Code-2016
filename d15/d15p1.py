puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

time = -1
found = False
while not found:
	time += 1
	time2 = time
	found = True
	for i in puzzle:
		time2 += 1
		if not (int(i.split(' ')[11][:-1]) + time2) % int(i.split(' ')[3]) == 0:
			found = False
			break

print time