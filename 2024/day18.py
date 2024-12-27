# DAY 18

# run it with pypy for faster execution

from collections import deque

X, Y = 71, 71
root, goal = (0, 0), (X-1, Y-1)

Map = [ [1] * Y for i in range(X) ]

with open('input18.txt') as f:
    for index, line in enumerate(f):
        if index == 1024:
            break

        x, y = line.strip().split(',')
        Map[int(y)][int(x)] = 0

def BFS():
    Q = deque()
    visited = set([root])
    Q.append(root + (0,))
    X, Y = len(Map), len(Map[0])

    def valid(x, y):
        return 0 <= x < X and 0 <= y < Y and Map[x][y]

    while Q:
        x, y, steps = Q.popleft()
        
        if (x, y) == goal:
            return steps

        for i, j in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if valid(i, j) and ( neighbor := (i, j) ) not in visited:
                visited.add(neighbor)
                Q.append((i, j, steps + 1))

    return -1

print(BFS())

#---------------------------------------------------------------------

from time import time

start = time()

with open('input18.txt') as f:
    for index, line in enumerate(f):
        if index >= 1024:
            x, y = line.strip().split(',')
            Map[int(y)][int(x)] = 0

            if BFS() == -1:
                print(x, y, time() - start)
                break