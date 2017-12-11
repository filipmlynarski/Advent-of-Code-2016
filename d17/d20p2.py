import hashlib
from copy import deepcopy
puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

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

#hash_object = hashlib.md5(b"" + costam)
#hash_object.hexdigest()

print puzzle