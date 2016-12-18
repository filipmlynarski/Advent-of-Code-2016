puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')

def get_idx(x):
	for j in x:
		for idx, i in enumerate(alphabet):
			if j == i:
				return idx
def contains(x, y):
	for i in x.split(' '):
		if y == i:
			return True
def change(x, add):
	ret = ''
	for i in x:
		for j in i:
			ret += alphabet[(int(add) + int(get_idx(j))) % len(alphabet)]
		ret += ' '
	return ret

for i in puzzle:
	if contains(change(i.split('[')[0].split('-')[:-1], i.split('-')[-1:][0].split('[')[0]), 'northpole'):
		print change(i.split('[')[0].split('-')[:-1], i.split('-')[-1:][0].split('[')[0])
		print i.split('-')[-1:][0].split('[')[0]