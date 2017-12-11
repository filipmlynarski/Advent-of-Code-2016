elfes = []
inp = 3017957
def zeros(x):
	ret = []
	for i in x:
		if i != 0:
			ret.append(i)
	return ret

def mhm(x, idx):
	if x[idx] == 0:
		return 1 + mhm(x, (idx + 1) % len(x))
	return 0

for i in range(inp):
	elfes.append(i + 1)

idx = -1
idx2 = -1
save = -1
while True:

	idx2 += 1
	idx += 1
	if elfes[idx % len(elfes)] == 0:
		#if len(zeros(elfes)) > 1:
		if len(elfes) < 5:
			print elfes
		idx += mhm(elfes, idx % len(elfes))
		#else:
			#elfes = zeros(elfes)
			#break

	idx %= len(elfes)

	if idx < save:
		
		idx = 0
		elfes = zeros(elfes)
		print len(elfes)
		#if len(elfes) < 5:
			#print elfes
		if len(elfes) == 1:
			break
	save = idx
	elfes[(idx2 + (len(elfes) + idx2) / 2) % len(elfes)] = 0

print zeros(elfes)
