from copy import deepcopy
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
				drogi.append([i,j,'0'])
def rem0ve(x):
	ret = []
	for i in range(len(x)):
		dont = False
		for j in range(i + 1, len(x)):
			if x[i] == x[j]:
				dont = True
		if not dont:
			ret.append(x[i])
	return ret
count = 0
done = False
maks = 1
import time
while not done:
	count += 1
	drogi2 = []
	for i in drogi:
		if puzzle[i[0] + 1][i[1]] != '#' and len(i[2] + puzzle[i[0] + 1][i[1]]) >= maks:
			if puzzle[i[0] + 1][i[1]] == '.':
				drogi2.append([i[0] + 1,i[1],i[2]])
			else:
				if not check(puzzle[i[0] + 1][i[1]], i[2]):
					if len(i[2] + puzzle[i[0] + 1][i[1]]) > maks:
						maks = len(i[2] + puzzle[i[0] + 1][i[1]])

					drogi2.append([i[0] + 1,i[1],i[2] + puzzle[i[0] + 1][i[1]]])
					if len(drogi2[len(drogi2) - 1][2]) == marks:
						done = True
				else:
					drogi2.append([i[0] + 1,i[1],i[2]])

		if puzzle[i[0] - 1][i[1]] != '#' and len(i[2] + puzzle[i[0] - 1][i[1]]) >= maks:
			if puzzle[i[0] - 1][i[1]] == '.':
				drogi2.append([i[0] - 1,i[1],i[2]])
			else:
				if not check(puzzle[i[0] - 1][i[1]], i[2]):
					if len(i[2] + puzzle[i[0] - 1][i[1]]) > maks:
						maks = len(i[2] + puzzle[i[0] - 1][i[1]])
					drogi2.append([i[0] - 1,i[1],i[2] + puzzle[i[0] - 1][i[1]]])
					if len(drogi2[len(drogi2) - 1][2]) == marks:
						done = True
				else:
					drogi2.append([i[0] - 1,i[1],i[2]])
						

		if puzzle[i[0]][i[1] + 1] != '#' and len(i[2] + puzzle[i[0]][i[1] + 1]) >= maks:
			if puzzle[i[0]][i[1] + 1] == '.':
				drogi2.append([i[0],i[1] + 1,i[2]])
			else:
				if not check(puzzle[i[0]][i[1] + 1], i[2]):
					if len(i[2] + puzzle[i[0]][i[1] + 1]) > maks:
						maks = len(i[2] + puzzle[i[0]][i[1] + 1])
					drogi2.append([i[0],i[1] + 1,i[2] + puzzle[i[0]][i[1] + 1]])
					if len(drogi2[len(drogi2) - 1][2]) == marks:
						done = True
				else:
					drogi2.append([i[0] - 1,i[1],i[2]])
						

		if puzzle[i[0]][i[1] - 1] != '#' and len(i[2] + puzzle[i[0]][i[1] - 1]) >= maks:
			if puzzle[i[0]][i[1] - 1] == '.':
				drogi2.append([i[0],i[1] - 1,i[2]])
			else:
				if not check(puzzle[i[0]][i[1] - 1], i[2]):
					if len(i[2] + puzzle[i[0]][i[1] - 1]) > maks:
						maks = len(i[2] + puzzle[i[0]][i[1] - 1])
					drogi2.append([i[0],i[1] - 1,i[2] + puzzle[i[0]][i[1] - 1]])
					if len(drogi2[len(drogi2) - 1][2]) == marks:
						done = True
				else:
					drogi2.append([i[0],i[1] - 1,i[2]])

	drogi = deepcopy(rem0ve(drogi2))

	print count
	print len(drogi)
print count