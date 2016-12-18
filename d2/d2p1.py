puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])
x = 1
y = 1
final = ''
for i in puzzle:
	for j in i:
		if j == 'U':
			if y != 2:
				y += 1
		elif j == 'D':
			if y != 0:
				y -= 1
		elif j == 'R':
			if x != 2:
				x += 1
		else:
			if x != 0:
				x -= 1

	if x == 0 and y == 2:
		final += '1'
	elif x == 1 and y == 2:
		final += '2'
	elif x == 2 and y == 2:
		final += '3'
	elif x == 0 and y == 1:
		final += '4'
	elif x == 1 and y == 1:
		final += '5'
	elif x == 2 and y == 1:
		final += '6'
	elif x == 0 and y == 0:
		final += '7'
	elif x == 1 and y == 0:
		final += '8'
	elif x == 2 and y == 0:
		final += '9'
	x = 1
	y = 1

print final