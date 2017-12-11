def any(number, base):
	new = ''
	while number != 0:
		i = 0
		while base ** i < number:
			i += 1
		new += ?
		number -= base ** (i - 1)