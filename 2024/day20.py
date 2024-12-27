# DAY 20

# run it with pypy for faster execution

from collections import defaultdict
from collections import deque
import re

with open('input20.txt') as f:
    Map, cheats = [], set()

    for row, line in enumerate(f):
        Map.append(list(line.strip()))

        if (cols := line.find('S')) != -1:
            root = (row, cols)
            Map[row][cols] = '.'

        elif (cole := line.find('E')) != -1:
            goal = (row, cole)
            Map[row][cole] = '.'
        
        cheats.update([ (row, m.start() + 1) for m in re.finditer('(?=\.#\.)', ''.join(Map[-1])) ])

for row, line in enumerate(zip(*Map)):
    cheats.update([ (m.start() + 1, row) for m in re.finditer('(?=\.#\.)', ''.join(line)) ])

X, Y = len(Map), len(Map[0])

#DFS could also work here...
def BFS(root, goal, Costs, path):
    Q, visited = deque([root + (0,)]), set([root])
    
    def valid(x, y):
        return 0 <= x < X and 0 <= y < Y and Map[x][y] != '#'

    while Q:
        x, y, steps = Q.popleft()

        Costs[(x, y)] = steps
        path.append((x, y))
        
        if (x, y) == goal:
            return steps

        for i, j in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if valid(i, j) and ( neighbor := (i, j) ) not in visited:
                visited.add(neighbor)
                Q.append((i, j, steps + 1))

    return -1

def manhattanDist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def computeCheats(Costs, path, maxDist, limit = 100):
    saveCheats = defaultdict(int)

    for i in range(len(path)):
        for j in range(i, len(path)):
            if (dist := manhattanDist(path[i], path[j])) <= maxDist:
                saveCheats[Costs[path[j]] - Costs[path[i]] - dist] += 1

    return sum( saveCheats[key] for key in saveCheats if key >= limit )

Costs, path = { root : 0 }, []

BFS(root, goal, Costs, path)

print(computeCheats(Costs, path, 2))
print(computeCheats(Costs, path, 20))