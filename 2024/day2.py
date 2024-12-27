# DAY 2

def is_safe(levels):

	if len(levels) < 2:
		return True
	
	diff = levels[1] - levels[0]

	if diff == 0 or abs(diff) > 3:
		return False

	positive = diff > 0

	for index in range(2, len(levels)):
		diff = levels[index] - levels[index - 1]

		if diff == 0 or abs(diff) > 3:
			return False

		if ( positive != ( diff > 0 ) ):
			return False

	return True

def is_trully_safe(levels):
	for index in range(len(levels)):
		copy = levels.copy()

		del copy[index]

		if is_safe(copy):
			return True

with open("input2.txt") as f:
	safe, trully_safe = 0, 0

	for line in f:
		level = list(map(int, line.split(' ')))

		if is_safe(level):
			safe += 1

		if is_trully_safe(level):		
			trully_safe += 1

	print(safe, trully_safe)