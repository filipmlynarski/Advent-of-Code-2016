puzle = open('puzzle')
puzzle = []

for i in puzle:
	puzzle.append(i.split('\n')[0])

def is_int(x):
	ints = '1,2,3,4,5,6,7,8,9,0'.split(',')
	for j in ints:
		if j == x:
			return True
import time
import sys
a = 0
first_a = -1
b = 0
c = 0
d = 0
done = False
def check(x):
	for idx, i in enumerate(x):
		if idx % 2 == 0:
			if i != '0':
				return False
		else:
			if i != '1':
				return False
	return True

while not done:

	a = 0
	b = 0
	c = 0
	d = 0

	first_a += 1
	a = first_a
	print a
	save = ''
	count = 0
	while count < len(puzzle):
		i = puzzle[count]
		if i.split(' ')[0] == 'cpy':
			if i.split(' ')[2] == 'a':
				if is_int(i.split(' ')[1][0]):
					a = int(i.split(' ')[1])
				else:
					if i.split(' ')[1] == 'b':
						a = b
					elif i.split(' ')[1] == 'c':
						a = c
					else:
						a = d

			elif i.split(' ')[2] == 'b':
				if is_int(i.split(' ')[1][0]):
					b = int(i.split(' ')[1])
				else:
					if i.split(' ')[1] == 'a':
						b = a
					elif i.split(' ')[1] == 'c':
						b = c
					else:
						b = d
			elif i.split(' ')[2] == 'c':
				if is_int(i.split(' ')[1][0]):
					c = int(i.split(' ')[1])
				else:
					if i.split(' ')[1] == 'b':
						c = b
					elif i.split(' ')[1] == 'a':
						c = a
					else:
						c = d
			elif i.split(' ')[2] == 'd':
				if is_int(i.split(' ')[1][0]):
					d = int(i.split(' ')[1])
				else:
					if i.split(' ')[2] == 'b':
						d = b
					elif i.split(' ')[2] == 'c':
						d = c
					else:
						d = a
		elif i.split(' ')[0] == 'inc':
			if i.split(' ')[1] == 'a':
				a += 1
			elif i.split(' ')[1] == 'b':
				b += 1
			elif i.split(' ')[1] == 'c':
				c += 1
			else:
				d += 1

		elif i.split(' ')[0] == 'dec':
			if i.split(' ')[1] == 'a':
				a -= 1
			elif i.split(' ')[1] == 'b':
				b -= 1
			elif i.split(' ')[1] == 'c':
				c -= 1
			else:
				d -= 1
		elif i.split(' ')[0] == 'jnz':
			if (is_int(i.split(' ')[1][0]) and i.split(' ')[1] != '0'):
				count += int(i.split(' ')[2]) - 1
			elif (i.split(' ')[1] == 'a' and a != 0):
				count += int(i.split(' ')[2]) - 1
			elif (i.split(' ')[1] == 'b' and b != 0):
				count += int(i.split(' ')[2]) - 1
			elif (i.split(' ')[1] == 'c' and c != 0):
				count += int(i.split(' ')[2]) - 1
			elif (i.split(' ')[1] == 'd' and d != 0):
				count += int(i.split(' ')[2]) - 1
		else:
			save += str(b)
			if not check(save):
				break
				
			elif len(save) > 100:
				print first_a
				done = True
				break

		count += 1

print first_a