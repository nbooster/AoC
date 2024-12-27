# DAY 21

from functools import lru_cache
from itertools import product
from time import time

def findShortestPaths(X, Y, root, goal, blockedCells):
    paths, pathSoFar, visited, minLength = [], [], set(), float('inf')

    def valid(cell):
        return 0 <= cell[0] < X and 0 <= cell[1] < Y and cell not in blockedCells

    def DFS(current, direction):
        nonlocal minLength

        if not valid(current) or current in visited or len(pathSoFar) > minLength:
            return

        if current == goal:
            minLength = len(pathSoFar)
            paths.append(''.join(pathSoFar + [direction + 'A']))
            return

        pathSoFar.append(direction)
        visited.add(current)

        x, y = current

        for x, y, d in ((x-1, y, '^'), (x+1, y, 'v'), (x, y-1, '<'), (x, y+1, '>')):
            DFS((x, y), d)

        pathSoFar.pop()
        visited.remove(current)

        return

    DFS(root, '')

    #return paths

    minMoves = controllerMoves(min(paths, key = controllerMoves))

    return tuple( path for path in paths if controllerMoves(path) == minMoves )

def getAllShortestPaths(Map):
    X, Y, P = len(Map), len(Map[0]), dict()
    cells = tuple(product(range(X), range(Y)))
    blockedCells = set( (x, y) for x, y in cells if Map[x][y].isspace() )

    for root, goal in product(cells, cells):
        if root not in blockedCells and goal not in blockedCells:
            P[str(Map[root[0]][root[1]]) + str(Map[goal[0]][goal[1]])] = findShortestPaths(X, Y, root, goal, blockedCells)

    return P

def manahattanDist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def controllerMoves(sequence):
    return sum( manahattanDist(ControllerDict[a], ControllerDict[b]) + 1 for a, b in zip(startCell + sequence, sequence) )

def getNumpadSequences(Map, sequence):
    return [ ''.join(t) for t in product( *[ Map[a+b] for a, b in zip(startCell + sequence, sequence) ] ) ]

@lru_cache(maxsize=None)
def getBestSequenceLengthRecursive(sequence, level = 0):
    sequencies = [ ControllerMap[a+b] for a, b in zip(startCell + sequence, sequence) ]

    if level == 0:
        return min( sum(len(i) for i in t) for t in product(*sequencies) )

    return min( sum( getBestSequenceLengthRecursive(s, level - 1) for s in t ) for t in product(*sequencies) )

def getBestSequenceLength(code, robots):
    return min( getBestSequenceLengthRecursive(seq, robots) for seq in getNumpadSequences(NumpadMap, code) )

start = time()

startCell = 'A'
Numpad = ['789', '456', '123', ' 0A']
Controller = [' ^A', '<v>']
ControllerDict = { '^' : (0, 1), 'A' : (0, 2), '<' : (1, 0), 'v' : (1, 1), '>' : (1, 2) }

NumpadMap, ControllerMap = getAllShortestPaths(Numpad), getAllShortestPaths(Controller)

with open('input21.txt') as f:
    codes = tuple( line.strip() for line in f.readlines() )

#codes = ('208A', '586A', '341A', '463A', '593A')
#codes = ('029A', '980A', '179A', '456A', '379A')

result1 = sum( int(code[:-1]) * getBestSequenceLength(code, 1) for code in codes )
result2 = sum( int(code[:-1]) * getBestSequenceLength(code, 24) for code in codes )

print(result1, result2, time() - start)
