puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])
x = 0
y = 2
araj = [['','','D','',''],['','A','B','C',''],['5','6','7','8','9'],['','2','3','4',''],['','','1','','']]
final = ''
for i in puzzle:
	for j in i:
		if j == 'U':
			if y + 1 < 5:
				if len(araj[y + 1][x]) > 0:
					y += 1
		elif j == 'D':
			if y - 1 > -1:
				if len(araj[y - 1][x]) > 0:
					y -= 1
		elif j == 'R':
			if x + 1 < 5:
				if len(araj[y][x + 1]) > 0:
					x += 1
		elif j == 'L':
			if x - 1 > -1:
				if len(araj[y][x - 1]) > 0:
					x -= 1
	
	final += araj[y][x]

print final