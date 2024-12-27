# DAY 13

import re
from math import isclose
import numpy as np

with open('input13.txt') as f:
    machines, XA, YA, XB, YB, XP, YP = [], 0, 0, 0, 0, 0, 0

    for line in f:
        line = line.strip()

        if line == '':
            machines.append((XA, YA, XB, YB, XP, YP))
            continue

        if 'A' in line:
            XA, YA = [ int(s) for s in re.findall(r'\d+', line) ]
        elif 'B' in line:
            XB, YB = [ int(s) for s in re.findall(r'\d+', line) ]
        else:
            XP, YP = [ int(s) for s in re.findall(r'\d+', line) ]

    machines.append((XA, YA, XB, YB, XP, YP))

result = 0
part2 = 10000000000000 #0
RT = 1 / part2

for XA, YA, XB, YB, XP, YP in machines:
    a, b = np.linalg.solve(np.array([[XA, XB], [YA, YB]]), np.array([XP + part2, YP + part2]))
    ra, rb = round(a), round(b)

    if isclose(a, ra, rel_tol=RT) and isclose(b, rb, rel_tol=RT):
        result += 3 * ra + rb

print(result)
