puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')

def idxx(x):
	ret = 0
	idxxxx = 0
	for idx, i in enumerate(x):
		if i > ret:
			ret = i
			idxxxx = idx
	return idxxxx

def join(x):
	ret = ''
	for i in x:
		ret += i
	return ret

def common(x):
	amoutn2 = []
	for i in alphabet:
		amoutn2.append(0)
	for i in x:
		for idx, j in enumerate(alphabet):
			if i == j:
				amoutn2[idx] += 1
	return alphabet[idxx(amoutn2)]

def check(x):
	ret = ''
	save = str(x.split('[')[1].split(']')[0])
	x = join(x.split('-')[:-1])
	for i in range(5):
		ret += str(common(x))[0]
		x = x.split(str(common(x))[0])
		x = join(x)
	if save == ret:
		return True
	return False

final = 0
for i in puzzle:
	if check(i):
		final += int(i.split('[')[0].split('-')[len(i.split('[')[0].split('-')) - 1])
print final