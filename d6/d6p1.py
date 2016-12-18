puzle = open('puzzle')
puzzle = []
for i in puzle:
	puzzle.append(i.split('\n')[0])

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
amoutn = []
for i in alphabet:
	amoutn.append(0)
def idxx(x):
	ret = 0
	idxxxx = 0
	for idx, i in enumerate(x):
		if i > ret:
			ret = i
			idxxxx = idx
	return idxxxx
def common(x):
	global alphabet
	global amoutn
	global idxx
	amoutn2 = []
	for i in alphabet:
		amoutn2.append(0)
	for i in x:
		for idx, j in enumerate(alphabet):
			if i == j:
				amoutn2[idx] += 1
	return alphabet[idxx(amoutn2)]
save = []
save2 = -1
final = ''
for i in range(len(puzzle[0])):
	save2 += 1
	save.append('')
	for j in puzzle:
		save[len(save) - 1] += j[save2]
	final += common(save[len(save) - 1])
print final