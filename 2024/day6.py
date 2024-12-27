# DAY 6

# run it with pypy for faster execution

def findStartPosition(lines):
    for i, line in enumerate(lines):
        for j, item in enumerate(line):
            if item == '^':
                return (i, j)
    return (0,0)

with open('input6.txt') as f:
    lines = [ line.strip() for line in f ]

rows, cols, pos, obstacle = len(lines), len(lines[0]), findStartPosition(lines), '#'

def run(lines, pos, direction):
    visited = { pos : None }
    obstacles = {}

    while True:
        x, y = pos

        if direction == 'U':
            for i in range(x-1, -1, -1):
                if lines[i][y] != obstacle:
                    visited[(i, y)] = None
                else:
                    pos = (i+1, y)
                    break

            else:
                break

            direction = 'R'

        elif direction == 'D':
            for i in range(x+1, rows):
                if lines[i][y] != obstacle:
                    visited[(i, y)] = None
                else:
                    pos = (i-1, y)
                    break

            else:
                break

            direction = 'L'

        elif direction == 'R':
            for j in range(y+1, cols):
                if lines[x][j] != obstacle:
                    visited[(x, j)] = None
                else:
                    pos = (x, j-1)
                    break

            else:
                break

            direction = 'D'

        else:
            for j in range(y-1, -1, -1):
                if lines[x][j] != obstacle:
                    visited[(x, j)] = None
                else:
                    pos = (x, j+1)
                    break

            else:
                break

            direction = 'U'

        #resetBoard(prevPos, pos, direction, lines)

        if (entry := (pos, direction)) in obstacles:
            return visited, True
        else:
            obstacles[entry] = None

    return visited, False

print(len(run(lines, pos, 'U')[0]))

#---------------------------------------------------------------------------

startPos, lines, positions = pos, [ list(line) for line in lines ], 0

pathSquares = set(run(lines, startPos, 'U')[0].keys())
pathSquares.remove(startPos)

for x, y in pathSquares:
    if lines[x][y] == '.':
        lines[x][y] = obstacle

        if run(lines, startPos, 'U')[1]:
            positions += 1

        lines[x][y] = '.'

print(positions)