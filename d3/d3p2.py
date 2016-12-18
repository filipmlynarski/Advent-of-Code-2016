puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])
fast = []
def check(x):
	if int(x[0]) + int(x[1]) > int(x[2]) and int(x[1]) + int(x[2]) > int(x[0]) and int(x[2]) + int(x[0]) > int(x[1]):
		return True
	return False
	mini = min(x)
	x2 = []
	for i in x:
		if i != mini:
			x2.append(i)
	if int(mini) + int(min(x2)) >= int(max(x)):
		return True
	return False
count = 0
save = 0
save1 = []
for i in puzzle:
	if save < 3:
		save1.append(i)
	fast = []
	i = i.split(' ')
	for j in i:
		if j != '':
			fast.append(j)
	if check(fast):
		count += 1
print count