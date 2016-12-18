puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

def srsly(x):
	ret = [[],[]]
	saving = False
	save = ''
	save2 = ''
	for i in x:
		if saving:
			save += i
		else:
			save2 += i
		if i == '[':
			ret[1].append(save2[:-1])
			save2 = ''
			saving = True
		elif i == ']':
			ret[0].append(save[:-1])
			save = ''
			saving = False
	if len(save2) > 0:
		ret[1].append(save2)
	return ret

def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret

def if_is(x):
	for idx, i in enumerate(x):
		if idx < len(x) - 3:
			save = join([x[idx] for i in range(4)])
			if x[idx] == x[idx + 3] and x[idx + 1] == x[idx + 2] and x[idx: idx + 4] != save:
				return True
	return False

def check_1(x):
	for idx, i in enumerate(x):
		if idx < len(x) - 3:
			if if_is(x[idx:idx + 4]):
				return True
	return False
sinal = 0

for i in puzzle:
	snow = False
	for j in srsly(i)[0]:
		if not snow and check_1(j):
			snow = True
	shine = False
	for j in srsly(i)[1]:
		if shine or check_1(j):
			shine = True

	if not snow and shine:
		sinal += 1
		
print sinal