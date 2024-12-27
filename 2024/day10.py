# DAY 10

from itertools import product

with open('input10.txt') as f:
    Map = tuple( tuple( int(x) for x in line.strip() ) for line in f )

nines, paths, X, Y , result1, result2 = set(), 0, len(Map), len(Map[0]), 0, 0

def DFS(x, y, prev):
    global nines, paths, X, Y, Map

    if x < 0 or x >= X or y < 0 or y >= Y: return

    current = Map[x][y]

    if current != prev + 1: return

    if current == 9:
        nines.add((x, y))
        paths += 1
        return

    DFS(x + 1, y, current)
    DFS(x - 1, y, current)
    DFS(x, y + 1, current)
    DFS(x, y - 1, current)

for x, y in product(range(X), range(Y)):
    if Map[x][y] == 0:
        nines.clear()
        paths = 0
        DFS(x, y, -1)
        result1 += len(nines)
        result2 += paths

print(result1, result2)