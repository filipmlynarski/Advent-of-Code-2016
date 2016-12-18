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

final = 0

while final < 64:

	i+=1
	hash_object = hashlib.md5(b"ngcjuoqr"+str(i))
	hasz = hash_object.hexdigest()

	if contains(hasz)[0]:

		letter = contains(hasz)[1]
		stop = False

		for j in range(i + 1, i + 1001):
			if not stop:

				hash_object = hashlib.md5(b"ngcjuoqr"+str(j))
				hasz = hash_object.hexdigest()

				if contains2(hasz, letter):
					final += 1
					print final
					break
print i