puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

def check(x):
	if x[0] == '^' and x[1] == '^' and x[2] == '.':
		return True
	elif x[0] == '.' and x[1] == '^' and x[2] == '^':
		return True
	elif x[0] == '.' and x[1] == '.' and x[2] == '^':
		return True
	elif x[0] == '^' and x[1] == '.' and x[2] == '.':
		return True
	return False
puzzle = ['^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^.']
for i in range(400000 - 1):
	puzzle.append('')
	for idx in range(len(puzzle[0])):
		if idx == 0 and check('.' + puzzle[len(puzzle) - 2][idx:idx + 2]):
			puzzle[len(puzzle) - 1] += '^'
		elif idx == len(puzzle[0]) - 1 and check(puzzle[len(puzzle) - 2][idx - 1:idx + 2] + '.'):
			puzzle[len(puzzle) - 1] += '^'
		elif idx != 0 and idx != len(puzzle[0]) - 1 and check(puzzle[len(puzzle) - 2][idx - 1: idx + 2]):
			puzzle[len(puzzle) - 1] += '^'
		else:
			puzzle[len(puzzle) - 1] += '.'
print 'done'
count = 0
for i in puzzle:
	for j in i:
		if j == '.':
			count += 1
print count