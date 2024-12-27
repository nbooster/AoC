# DAY 12

from itertools import product

def calculateBlockPerimeter(i, j):
    global X, Y, garden
    
    current, per = garden[i][j], 0

    if i in (0, X-1): per += 1
    if j in (0, Y-1): per += 1

    if i and garden[i-1][j] != current: per += 1
    if i < X - 1 and garden[i+1][j] != current: per += 1
    
    if j and garden[i][j-1] != current: per += 1
    if j < Y - 1 and garden[i][j+1] != current: per += 1

    return per

def findRegion(i, j):
    global X, Y, garden, visited, region, symbol

    if i in (-1, X) or j in (-1, Y) or visited[i][j] or garden[i][j] != symbol: return

    visited[i][j] = True

    if garden[i][j] == symbol: region.append((i, j))

    findRegion(i+1, j)
    findRegion(i-1, j)
    findRegion(i, j+1)
    findRegion(i, j-1)

def calculateSides(region):
    global X, Y, garden

    def downEdge(x, y, symbol):
        global garden
        return x == X - 1 or garden[x+1][y] != symbol

    def upEdge(x, y, symbol):
        global garden
        return x == 0 or garden[x-1][y] != symbol

    def rightEdge(x, y, symbol):
        global garden
        return y == Y - 1 or garden[x][y+1] != symbol

    def leftEdge(x, y, symbol):
        global garden
        return y == 0 or garden[x][y-1] != symbol

    def countEdgesHorizontal(blocks):
        if len(blocks) <= 1: return len(blocks)
        return 1 + sum( 1 for i in range(1, len(blocks)) if abs(blocks[i][1] - blocks[i-1][1]) > 1 )

    def countEdgesVertical(blocks):
        if len(blocks) <= 1: return len(blocks)
        return 1 + sum( 1 for i in range(1, len(blocks)) if abs(blocks[i][0] - blocks[i-1][0]) > 1 )

    perimeter, symbol = dict(), garden[region[0][0]][region[0][1]]

    for i, j in region:
        if i in (0, X-1) or j in (0, Y-1) or not (symbol == garden[i-1][j] == garden[i+1][j] == garden[i][j-1] == garden[i][j+1]):
            perimeter[(i,j)] = None

    minX, maxX, minY, maxY = X, 0, Y, 0

    for x, y in perimeter:
        if x < minX: minX = x
        if x > maxX: maxX = x

        if y < minY: minY = y
        if y > maxY: maxY = y

    sides = 0

    for x in range(minX, maxX + 1):
        horizontal = [ (x,y) for y in range(minY, maxY + 1) if (x,y) in perimeter ]
        horUp = [ (x,y) for x, y in horizontal if upEdge(x,y,symbol) ]
        horDown = [ (x,y) for x, y in horizontal if downEdge(x,y,symbol) ]
        
        sides += countEdgesHorizontal(horUp) + countEdgesHorizontal(horDown)

    for y in range(minY, maxY + 1):
        vertical = [ (x,y) for x in range(minX, maxX + 1) if (x,y) in perimeter ]
        vertLeft = [ (x,y) for x, y in vertical if leftEdge(x,y,symbol) ]
        vertRight = [ (x,y) for x, y in vertical if rightEdge(x,y,symbol) ]
        
        sides += countEdgesVertical(vertLeft) + countEdgesVertical(vertRight)

    return sides

with open('input12.txt') as f:
    garden = [ line.strip() for line in f ]

regions, X, Y, region, visited = [], len(garden), len(garden[0]), [], [ [False] * len(garden[0]) for i in range(len(garden)) ]

for i, j in product(range(X), range(Y)):
    symbol = garden[i][j]

    findRegion(i, j)

    if region:
        regions.append(region.copy())

    region.clear()

result1 = sum( len(region) * sum( calculateBlockPerimeter(i,j) for i, j in region ) for region in regions )

result2 = sum( len(region) * calculateSides(region) for region in regions )

print(result1, result2)