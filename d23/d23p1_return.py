puzzle = open('puzzle').read().splitlines()
registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
i = 0
def dig(x):
	return x.split('-')[-1].isdigit()
import time
while i < len(puzzle):
	p = puzzle[i].split(' ')
	if 'cpy' in puzzle[i]:
		if dig(p[1]):
			registers[p[2]] = int(p[1])
		elif p[1] in 'abcd':
			registers[p[2]] = registers[p[1]]
	elif 'inc' in puzzle[i] and p[1] in 'abcd':
		registers[p[1]] += 1
	elif 'dec' in puzzle[i] and p[1] in 'abcd':
		registers[p[1]] -= 1
	elif 'jnz' in puzzle[i]:
		if (dig(p[1]) and p[1] != '0') or (p[1] in 'abcd' and not dig(p[1]) and registers[p[1]] != 0):
			if dig(p[2]):
				i += int(p[2]) - 1
			elif p[2] in 'abcd':
				i += registers[p[2]] - 1
	elif 'tgl' in puzzle[i]:
		if p[1] in 'abcd':
			p[1] = registers[p[1]]
		if int(p[1]) + i < len(puzzle):
			if len(puzzle[int(p[1]) + i].split(' ')) == 2:
				if puzzle[int(p[1]) + i].split(' ')[0] == 'inc':
					puzzle[int(p[1]) + i] = 'dec ' + ' '.join(puzzle[int(p[1]) + i].split(' ')[1:])
				else:
					puzzle[int(p[1]) + i] = 'inc ' + ' '.join(puzzle[int(p[1]) + i].split(' ')[1:])
			elif len(puzzle[int(p[1]) + i].split(' ')) == 3:
				if puzzle[int(p[1]) + i].split(' ')[0] == 'jnz':
					puzzle[int(p[1]) + i] = 'cpy ' + ' '.join(puzzle[int(p[1]) + i].split(' ')[1:])
				else:
					puzzle[int(p[1]) + i] = 'jnz ' + ' '.join(puzzle[int(p[1]) + i].split(' ')[1:])
	i += 1
print registers['a']
'479010906'