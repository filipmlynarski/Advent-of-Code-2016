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

def look_for(x, y):
	for i in y:
		for idx, letter in enumerate(i):
			if idx < len(i) - 2:
				if i[idx: idx + 3] == x:
					return True
	return False

def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret
final = 0
for i in puzzle:
	done = False
	sejwik = srsly(i)[0]
	for j in srsly(i)[1]:
		for idx, letter in enumerate(j):
			if idx < len(j) - 2:
				save = join([letter for w in range(3)])
				if j[idx] == j[idx + 2] and j[idx: idx + 3] != save:
					if look_for(j[idx + 1] + j[idx] + j[idx + 1], sejwik):
						done = True
	if done:
		final += 1

print final