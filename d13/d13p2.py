from copy import deepcopy

puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])
done = False
def dec_to_bin(x):
    return int(bin(x)[2:])
def check(two):
	x = two[0]
	y = two[1]
	count = 0
	for i in str(dec_to_bin(x*x + 3*x + 2*x*y + y + y*y + 1358)):
		if i == '1':
			count += 1
	if count % 2 == 0:
		return True
	return False
def przesiew(x, y):
	for i in y:
		if i == x:
			return True
	return False

add = 0
positions = [[1,1]]
positions2 = []
final = []
while add < 50:
	add += 1
	for i in positions:

		if i[1] - 1 >= 0 and check([i[0], i[1] - 1]) and not przesiew([i[0], i[1] - 1], positions2):
			positions2.append([i[0], i[1] - 1])

		if check([i[0], i[1] + 1]) and not przesiew([i[0], i[1] + 1], positions2):
			positions2.append([i[0] ,i[1] + 1])

		if check([i[0] + 1, i[1]]) and not przesiew([i[0] + 1, i[1]], positions2):
			positions2.append([i[0] + 1, i[1]])

		if i[0] - 1 >= 0 and check([i[0] - 1, i[1]]) and not przesiew([i[0] - 1, i[1]], positions2):
			positions2.append([i[0] - 1, i[1]])

	positions = positions2
	positions2 = []
	for i in positions:
		if not przesiew(i, final):
			final.append(i)

print len(final)