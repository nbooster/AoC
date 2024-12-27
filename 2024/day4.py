# DAY 4

xmas = 0

expression = 'XMAS'

with open('input4.txt') as f:
	lines = f.readlines()

lines = [ line.strip() for line in lines ]

from collections import defaultdict

def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

cols = [ ''.join(line) for line in groups(lines, lambda x, y: x) ]
rows = [ ''.join(line) for line in groups(lines, lambda x, y: y) ] # redundant
fdiag = [ ''.join(line) for line in groups(lines, lambda x, y: x + y) ]
bdiag = [ ''.join(line) for line in groups(lines, lambda x, y: x - y) ]

import re

for line in rows + cols + fdiag + bdiag:
	xmas += sum(1 for m in re.finditer(expression, line)) + sum(1 for m in re.finditer(expression, line[::-1]))

print(xmas)

#----------------------------------------------------------------------------------------------------------------

import itertools

x_mas = 0

T = ('M', 'S')

for x, y in itertools.product(range(1, len(lines) - 1), range(1, len(lines[0]) - 1)):
    if lines[x][y] == 'A':
    	ul, ur, dl, dr = lines[x-1][y-1], lines[x-1][y+1], lines[x+1][y-1], lines[x+1][y+1]

    	if ul in T and dr in T and ul != dr and ur in T and dl in T and ur != dl:
    		x_mas += 1

print(x_mas)