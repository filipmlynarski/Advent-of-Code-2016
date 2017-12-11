puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

def mininum_val(x):
	ret = x[0]
	save = 0 
	for idx, i in enumerate(x):
		if ret > i:
			ret = i
			save = idx
	return [ret, save]
def sort(x):
	new = []
	for i in x:
		new.append(int(i.split('-')[0]))
	ret = []
	for i in new:
		ret.append(x[mininum_val(new)[1]])
		new[mininum_val(new)[1]] = 4294967295

	return ret

puzzle = sort(puzzle)
now = 0
stop = False

while not stop:
	for i in puzzle:
		if now < int(i.split('-')[0]) or now > int(i.split('-')[1]):
			stop = True
		else:
			stop = False
			now = int(i.split('-')[1]) + 1
			break
	if stop:
		print now
		break