import hashlib
i=-1

def contains(x):
	for idx, i in enumerate(x):
		if idx < len(x) - 2:
			if i * 3 == x[idx:idx + 3]:
				return [True, i]
	return [False]
def contains2(x, y):
	for idx, i in enumerate(x):
		if idx < len(x) - 4:
			if y * 5 == x[idx:idx + 5]:
				return True
	return False
def times2016(x):
	for i in range(2017):
		x = hashlib.md5(b""+x).hexdigest()
	return x

final = 0
hasze = []

while final < 64:

	i+=1

	if i == len(hasze):
		hasze.append(times2016("ngcjuoqr"+str(i)))

	hasz = hasze[i]

	if contains(hasz)[0]:

		letter = contains(hasz)[1]
		stop = False

		for j in range(i + 1, i + 1001):
			if j >= len(hasze):
				hasze.append(times2016("ngcjuoqr"+str(j)))

		for j in range(i + 1, i + 1001):
			if contains2(hasze[j], letter):
				final += 1
				print final

print i