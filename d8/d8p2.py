from copy import deepcopy
import numpy as np
import time
puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

def swap(x, idx, swaper):
	ret = ''
	for idx2, i in enumerate(x):
		if idx2 == idx:
			ret += swaper
		else:
			ret += i
	return ret

def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret

yy = 6
xx = 50

def push(x, y):
	x2 = deepcopy(x)
	for i in range(len(x) - 1):
		x2[i + 1][y] = x[i][y]
	x2[0][y] = x[len(x) - 1][y]
	return x2
def push2(x, y):
	x2 = deepcopy(x)
	x2[y][1:] = x[y][:-1]
	x2[y][0] = x[y][len(x[y]) - 1]
	return x2

screen = []
for y in range(yy):
	screen.append([])
	for x in range(xx):
		screen[len(screen) - 1].append('.')
screen2 = []
for i in puzzle:
	screen2 = deepcopy(screen)
	if i.split(' ')[0] == 'rect':
		for y in range(yy):
			for x in range(xx):
				if y < int(i.split(' ')[1].split('x')[1]) and x < int(i.split(' ')[1].split('x')[0]):
					screen2[y][x] = '#'

	if i.split(' ')[1] == 'column':
		for x in range(int(i.split(' ')[4])):
			screen2 = push(screen2, int(i.split(' ')[2].split('=')[1]))

	elif i.split(' ')[1] == 'row':
		for x in range(int(i.split(' ')[4])):
			screen2 = push2(screen2, int(i.split(' ')[2].split('=')[1]))
	screen = deepcopy(screen2)

	for i in screen:
		print ' ' + join(i)
	time.sleep(0.05)

#for i in screen:
	#print join(i)