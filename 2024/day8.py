# DAY 8

from collections import defaultdict
from itertools import combinations

Antennas = defaultdict(list)
antinodes = set()

with open('input8.txt') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c not in '.\n':
                Antennas[c].append((i, j))
                antinodes.add((i, j))

X, Y = len(lines), len(lines[0]) - 1

for c, positions in Antennas.items():
    for t1, t2 in combinations(positions, 2):
        diffx, diffy = t2[0] - t1[0], t2[1] - t1[1]

        a = 1
        while True:
            a1x, a1y = t1[0] - a * diffx, t1[1] - a * diffy

            if 0 <= a1x < X and 0 <= a1y < Y:
                antinodes.add((a1x, a1y))
            else:
                break

            a += 1

        b = 1
        while True:
            a2x, a2y = t2[0] + b * diffx, t2[1] + b * diffy

            if 0 <= a2x < X and 0 <= a2y < Y:
                antinodes.add((a2x, a2y))
            else:
                break

            b += 1

        '''a1x, a1y = t1[0] - diffx, t1[1] - diffy
        a2x, a2y = t2[0] + diffx, t2[1] + diffy

        if 0 <= a1x < X and 0 <= a1y < Y:
            antinodes.add((a1x, a1y))

        if 0 <= a2x < X and 0 <= a2y < Y:
            antinodes.add((a2x, a2y))'''

print(len(antinodes))



