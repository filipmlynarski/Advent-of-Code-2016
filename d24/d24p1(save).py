from copy import deepcopy
import numpy as np
puzle = open('puzzle')
puzzle = []
def check(x, y):
	for i in y:
		if i == x:
			return True
	return False
for i in puzle:
	puzzle.append(i.split('\n')[0])
marks = 1
drogi = []
for i in range(len(puzzle)):
	for j in range(len(puzzle[i])):
		if puzzle[i][j] != '#' and puzzle[i][j] != '.':
			if puzzle[i][j] != '0':
				marks += 1
			else:
				drogi.append([[i,j],'0',[]])
print drogi
def rem0ve(x):
	ret = []
	for i in range(len(x)):
		dont = False
		for j in range(i + 1, len(x)):
			if x[i][:2] == x[j][:2]:
				dont = True
		if not dont:
			ret.append(x[i])
	return ret
def new_remove(x, maks):
	ret = []
	for i in x:
		if len(i[1]) >= maks:
			ret.append(i)
	return ret
count = 0
done = False
maks = 1

import time
while not done:
	count += 1
	drogi2 = []
	for i in drogi:
		if puzzle[i[0][0] + 1][i[0][1]] != '#' and [[i[0][0] + 1, i[0][1]]] != i[2]:# not check([i[0][0] + 1, i[0][1]], i[2]):
			if puzzle[i[0][0] + 1][i[0][1]] == '.':
				drogi2.append([[i[0][0] + 1,i[0][1]] ,i[1], [i[0]]])
			else:
				if not check(puzzle[i[0][0] + 1][i[0][1]], i[1]):
					#if len(i[1] + puzzle[i[0][0] + 1][i[0][1]]) > maks + 1:
						#maks = len(i[1] + puzzle[i[0][0] + 1][i[0][1]])
					drogi2.append([[i[0][0] + 1,i[0][1]],i[1] + puzzle[i[0][0] + 1][i[0][1]], []])
					if len(drogi2[len(drogi2) - 1][1]) == marks:
						done = True
				else:
					drogi2.append([[i[0][0] + 1,i[0][1]],i[1], [i[0]]])

		if puzzle[i[0][0] - 1][i[0][1]] != '#' and [[i[0][0] - 1, i[0][1]]] != i[2]: # not check([i[0][0] - 1, i[0][1]], i[2]):
			if puzzle[i[0][0] - 1][i[0][1]] == '.':
				drogi2.append([[i[0][0] - 1,i[0][1]], i[1], [i[0]]])
			else:
				if not check(puzzle[i[0][0] - 1][i[0][1]], i[1]):

					#if len(i[1] + puzzle[i[0][0] - 1][i[0][1]]) > maks + 1:
						#maks = len(i[1] + puzzle[i[0][0] - 1][i[0][1]])

					drogi2.append([[i[0][0] - 1,i[0][1]],i[1] + puzzle[i[0][0] - 1][i[0][1]], []])
					if len(drogi2[len(drogi2) - 1][1]) == marks:
						done = True
				else:
					drogi2.append([[i[0][0] - 1,i[0][1]],i[1], [i[0]]])
						

		if puzzle[i[0][0]][i[0][1] + 1] != '#' and [[i[0][0], i[0][1] + 1]] != i[2]: #not check([i[0][0], i[0][1] + 1], i[2]):
			if puzzle[i[0][0]][i[0][1] + 1] == '.':
				drogi2.append([[i[0][0],i[0][1] + 1], i[1], [i[0]]])
			else:
				if not check(puzzle[i[0][0]][i[0][1] + 1], i[1]):

					#if len(i[1] + puzzle[i[0][0]][i[0][1] + 1]) > maks + 1:
						#maks = len(i[1] + puzzle[i[0][0]][i[0][1] + 1])

					drogi2.append([[i[0][0],i[0][1] + 1],i[1] + puzzle[i[0][0]][i[0][1] + 1], []])
					if len(drogi2[len(drogi2) - 1][1]) == marks:
						done = True
				else:
					drogi2.append([[i[0][0] - 1,i[0][1]],i[1], [i[0]]])

		if puzzle[i[0][0]][i[0][1] - 1] != '#' and [[i[0][0], i[0][1] - 1]] != i[2] :#not check([i[0][0], i[0][1] - 1], i[2]):

			if puzzle[i[0][0]][i[0][1] - 1] == '.':
				drogi2.append([[i[0][0],i[0][1] - 1], i[1], [i[0]]])
			else:
				if not check(puzzle[i[0][0]][i[0][1] - 1], i[1]):

					#if len(i[1] + puzzle[i[0][0]][i[0][1] - 1]) > maks + 1:
						#maks = len(i[1] + puzzle[i[0][0]][i[0][1] - 1])

					drogi2.append([[i[0][0],i[0][1] - 1],i[1] + puzzle[i[0][0]][i[0][1] - 1], []])
					if len(drogi2[len(drogi2) - 1][1]) == marks:
						done = True
				else:
					drogi2.append([[i[0][0],i[0][1] - 1],i[1], [i[0]]])
	drogi = deepcopy(rem0ve(drogi2))

	print count
	print len(drogi)
	#print np.array(drogi)
	print 'maks =',maks

print count