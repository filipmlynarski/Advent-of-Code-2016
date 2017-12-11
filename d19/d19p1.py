def look(x, idx):
	first = -1
	while True:
		first += 1
		for i in range(len(x)):
			if first == 0 and i > idx:
				if x[i] != 0:
					return i
			elif first > 0:
				if x[i] != 0:
					return i
elfes = []
inp = 3017957
def idx(x):
	for idx, i in enumerate(x):
		if i != 0:
			return idx
def zeros(x):
	good = 0
	for i in x:
		if i != 0:
			good += 1
	return good
for i in range(inp):
	elfes.append(1)

save_idx = -1
while not zeros(elfes) == 1:

	for i in range(len(elfes)):
		if elfes[i] != 0 and save_idx == -1:
			save_idx = i

		elif elfes[i] != 0:

			elfes[i] = 0
			save_idx = -1

	print zeros(elfes)
print idx(elfes) + 1