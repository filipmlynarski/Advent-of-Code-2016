import hashlib
from copy import deepcopy
puzle = open('puzzle')
puzzle = []

def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret
def check(x, y):
	for i in y:
		if i == x:
			return True
	return False
def is_int(x):
	nmbrs = '0,1,2,3,4,5,6,7,8,9'.split(',')
	for i in nmbrs:
		if i == x:
			return True
	return False
for i in puzle:
	puzzle.append(i.split('\n')[0])
positions = [[0, 3]]
starting = 'njfxhljp'
path = [starting]
fast = 'U,D,L,R'.split(',')
save = 0
while len(positions) > 0:
	positions2 = []
	path2 = []
	for idx, i in enumerate(positions):
		for j in range(4):
			hash_object = hashlib.md5(b"" + path[idx])
			if not is_int(hash_object.hexdigest()[j]) and hash_object.hexdigest()[j] != 'a':
				if fast[j] == 'U' and i[1] != 3:
					positions2.append([i[0], i[1] + 1])
					path2.append(path[idx] + fast[j])
				elif fast[j] == 'D' and i[1] != 0:
					positions2.append([i[0], i[1] - 1])
					path2.append(path[idx] + fast[j])
				elif fast[j] == 'L' and i[0] != 0:
					positions2.append([i[0] - 1, i[1]])
					path2.append(path[idx] + fast[j])
				elif fast[j] == 'R' and i[0] != 3:
					positions2.append([i[0] + 1, i[1]])
					path2.append(path[idx] + fast[j])
				if len(positions2) > 0 and positions2[len(positions2) - 1] == [3, 0]:
					save = len(path2[len(path2) - 1].split(starting)[1])
					positions2 = deepcopy(positions2[:-1])
					path2 = deepcopy(path2[:-1])

	positions = deepcopy(positions2)
	path = deepcopy(path2)
print save
