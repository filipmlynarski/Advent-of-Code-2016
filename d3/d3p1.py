puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])
fast = []
def check(x):
	if int(x[0]) + int(x[1]) > int(x[2]) and int(x[1]) + int(x[2]) > int(x[0]) and int(x[2]) + int(x[0]) > int(x[1]):
		return True
	return False
def deelete(x):
	ret = []
	for i in x:
		if i != '':
			ret.append(i)
	return ret
count = 0
save = 0
save1 = []
for idx, i in enumerate(puzzle):
	save += 1
	save1.append(deelete(i.split(' ')))
	if idx % 3 == 2:
		save = 0
		fast = []
		if check([save1[0][0], save1[1][0], save1[2][0]]):
			count += 1
		if check([save1[0][1], save1[1][1], save1[2][1]]):
			count += 1
		if check([save1[0][2], save1[1][2], save1[2][2]]):
			count += 1
		save1 = []

print count