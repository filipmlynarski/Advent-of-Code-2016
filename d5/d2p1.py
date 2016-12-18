import hashlib
m = hashlib.md5()
i=-1
pas = '        '
def swap(x, idx, swaper):
	ret = ''
	for idx2, i in enumerate(x):
		if idx2 == idx:
			ret += swaper
		else:
			ret += i
	return ret
def spaces(x):
	for i in x:
		if i == ' ':
			return True
	return False
def isint(x):
	ints = '0,1,2,3,4,5,6,7'.split(",")
	for i in x:
		for j in ints:
			if i == j:
				return True
	return False

while spaces(pas):
	m = hashlib.md5()
	i+=1
	save = m.update("abbhdwsy"+str(i))
	sejw = m.hexdigest()
	if sejw[0:5]=="00000" and isint(sejw[5]) and pas[int(sejw[5])] == ' ':
		pas = swap(pas, int(sejw[5]), sejw[6]) 

print pas