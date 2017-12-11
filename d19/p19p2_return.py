elves = [i for i in range(3017957)]
i = 0
while len(elves) > 1:
	elves.pop((i + len(elves) / 2) % len(elves))
	i += 1
	if i % len(elves) != i:
		i = 0
	print len(elves)
print 'wynik: ' + str(elves[0] + 1)