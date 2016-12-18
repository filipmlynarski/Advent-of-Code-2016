import numpy as np

puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

looking_1 = 17
looking_2 = 61

robots = []
outputs = []

for i in puzzle:
	if i.split(' ')[0] == 'value':
		if int(i.split(' ')[5]) >= len(robots):
			for j in range(int(i.split(' ')[5]) - len(robots) + 2):
				robots.append([])
		robots[int(i.split(' ')[5])].append(int(i.split(' ')[1]))

not_done = True

while not_done:
	for i in puzzle:
		if i.split(' ')[0] != 'value':
			if int(i.split(' ')[1]) < len(robots) and len(robots[int(i.split(' ')[1])]) > 1:
				if robots[int(i.split(' ')[1])] == [looking_1, looking_2] or robots[int(i.split(' ')[1])] == [looking_2, looking_1]:
					print i.split(' ')[1]
					not_done = False

				if i.split(' ')[5] == 'bot':
					if int(i.split(' ')[6]) >= len(robots):
						for j in range(int(i.split(' ')[6]) - len(robots) + 2):
							robots.append([])
					robots[int(i.split(' ')[6])].append(np.min(robots[int(i.split(' ')[1])]))
				else:
					if int(i.split(' ')[6]) >= len(outputs):
						for j in range(int(i.split(' ')[6]) - len(outputs) + 2):
							outputs.append([])
					outputs[int(i.split(' ')[6])].append(np.min(robots[int(i.split(' ')[1])]))

				if i.split(' ')[10] == 'bot':
					robots[int(i.split(' ')[11])].append(np.max(robots[int(i.split(' ')[1])]))
				else:
					if int(i.split(' ')[11]) >= len(outputs):
						for j in range(int(i.split(' ')[11]) - len(outputs) + 2):
							outputs.append([])
					outputs[int(i.split(' ')[11])].append(np.max(robots[int(i.split(' ')[1])]))

				robots[int(i.split(' ')[1])] = []