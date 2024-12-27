# DAY 16

# run it with pypy for faster execution

with open('input16.txt') as f:
    Map = []

    for index, line in enumerate(f):
        line = line.strip()

        if ( SY := line.find('S') ) != -1:
            start = (index, SY)

        if ( EY := line.find('E') ) != -1:
            end = (index, EY)

        Map.append(list(line))

direction, visited, minScore, pathSoFar, bestTiles = '>', {}, float('inf'), [], set()

def solve1(position, direction, score):
    global Map, visited, minScore

    if score > minScore or score > visited.get(position, minScore): #or just: if score >= visited.get(position, minScore):
        return

    x, y = position

    if ( block := Map[x][y] ) == '#':
        return

    elif block == 'E':
        minScore = score
        return

    visited[position] = score
    
    if direction == '>':
        solve1((x-1, y), '^', score + 1001)
        solve1((x+1, y), 'v', score + 1001)
        solve1((x, y+1), '>', score + 1)

    elif direction == '<':
        solve1((x-1, y), '^', score + 1001)
        solve1((x+1, y), 'v', score + 1001)
        solve1((x, y-1), '<', score + 1)

    elif direction == '^':
        solve1((x-1, y), '^', score + 1)
        solve1((x, y+1), '>', score + 1001)
        solve1((x, y-1), '<', score + 1001)

    else:
        solve1((x+1, y), 'v', score + 1)
        solve1((x, y-1), '<', score + 1001)
        solve1((x, y+1), '>', score + 1001)

    return

def solve2(position, direction, score):
    global Map, visited, minScore

    pathSoFar.append(position)

    key = position + (direction,)

    if score > minScore or score > visited.get(key, minScore):
        pathSoFar.pop()
        return

    x, y = position

    if ( block := Map[x][y] ) == '#':
        pathSoFar.pop()
        return

    elif block == 'E' and score == minScore:
        bestTiles.update(pathSoFar)
        pathSoFar.pop()
        return
    
    visited[key] = score

    
    if direction == '>':
        solve2((x-1, y), '^', score + 1001)
        solve2((x+1, y), 'v', score + 1001)
        solve2((x, y+1), '>', score + 1)

    elif direction == '<':
        solve2((x-1, y), '^', score + 1001)
        solve2((x+1, y), 'v', score + 1001)
        solve2((x, y-1), '<', score + 1)

    elif direction == '^':
        solve2((x-1, y), '^', score + 1)
        solve2((x, y+1), '>', score + 1001)
        solve2((x, y-1), '<', score + 1001)

    else:
        solve2((x+1, y), 'v', score + 1)
        solve2((x, y-1), '<', score + 1001)
        solve2((x, y+1), '>', score + 1001)

    pathSoFar.pop()
    return

import sys

sys.setrecursionlimit(3000)

solve1(start, direction, 0)

result1 = minScore

print(result1)

visited.clear()

solve2(start, direction, 0)

result2 = len(bestTiles)

print(result2)