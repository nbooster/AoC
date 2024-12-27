# DAY 3

import re

expr1 = 'mul\((\d{1,3})\,(\d{1,3})\)'

with open("input3.txt") as f:
	rawInput = f.read()

mulsSum = sum( int(m[1]) * int(m[2]) for m in re.finditer(expr1, rawInput) )

print(mulsSum)

#---------------------------------------------------------------------------

expr2, expr3 = "do\(\)", "don't\(\)"

s, do = 0, True

for m in re.finditer("|".join([expr1, expr2, expr3]), rawInput):
	if ( text := m[0] ) == "do()":
		do = True

	elif text == "don't()":
		do = False

	else:
		if do:
			s += int(m[1]) * int(m[2])

print(s)