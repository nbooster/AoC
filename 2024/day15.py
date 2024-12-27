# DAY 15

def moveRight(Map, row, col):
    for j in range(col+1, len(Map[0])):
        if ( item := Map[row][j] ) != 'O':

            if item == '.':
                Map[row][col+1:j+1] = Map[row][col:j]
                Map[row][col] = '.'
                col += 1

            break

    return row, col

def moveLeft(Map, row, col):
    for j in range(col-1, -1, -1):
        if ( item := Map[row][j] ) != 'O':

            if item == '.':
                Map[row][col-1:j-1:-1] = Map[row][col:j:-1]
                Map[row][col] = '.'
                col -= 1

            break

    return row, col

def moveDown(Map, row, col):
    for i in range(row+1, len(Map)):
        if ( item := Map[i][col] ) != 'O':

            if item == '.':
                for ir in range(i, row, -1):
                    Map[ir][col] = Map[ir-1][col]
                Map[row][col] = '.'
                row += 1

            break

    return row, col

def moveUp(Map, row, col):
    for i in range(row-1, -1, -1):
        if ( item := Map[i][col] ) != 'O':

            if item == '.':
                for ir in range(i, row):
                    Map[ir][col] = Map[ir+1][col]
                Map[row][col] = '.'
                row -= 1

            break

    return row, col

with open('input15.txt') as f:
    Map, Moves = [], []
    Var, subNotFound = Map, True

    for index, line in enumerate(f):
        line = line.strip()

        if subNotFound:
            subCol = line.find('@')

            if subCol != -1:
                subRow = index
                subNotFound = False

        if line:
            Var.append(line)
        else:
            Var = Moves

    Map = [ list(row) for row in Map ]
    Moves = ''.join(Moves)

#---------------------------------------------------------
Map2 = []

for row in Map:
    row2 = []

    for item in row:
        if item in ('#', '.'): row2.extend([item] * 2)
        elif item == 'O': row2.extend(['[',']'])
        else: row2.extend(['@', '.'])

    Map2.append(row2)

subRow2, subCol2 = subRow, subCol * 2
#---------------------------------------------------------

for move in Moves:
    match move:
        case '^': subRow, subCol = moveUp(Map, subRow, subCol)
        case 'v': subRow, subCol = moveDown(Map, subRow, subCol)
        case '<': subRow, subCol = moveLeft(Map, subRow, subCol)
        case '>': subRow, subCol = moveRight(Map, subRow, subCol)
        case _: pass
    
from itertools import product

result1 = sum( 100 * row + col for row, col in product(range(len(Map)), range(len(Map[0]))) if Map[row][col] == 'O' )

print(result1)

#---------------------------------------------------------------------------------------------------------------

def moveRight2(Map, row, col):
    for j in range(col+1, len(Map[0])):
        if ( item := Map[row][j] ) not in '[]':

            if item == '.':
                Map[row][col+1:j+1] = Map[row][col:j]
                Map[row][col] = '.'
                col += 1

            break

    return row, col

def moveLeft2(Map, row, col):
    for j in range(col-1, -1, -1):
        if ( item := Map[row][j] ) not in '[]':

            if item == '.':
                Map[row][col-1:j-1:-1] = Map[row][col:j:-1]
                Map[row][col] = '.'
                col -= 1

            break

    return row, col

def moveDown2(Map, row, col):
    cellsToMove = {}

    def canMoveDown(i, j1, j2):
        nonlocal Map, cellsToMove

        downLeft, downRight = Map[i+1][j1], Map[i+1][j2]

        cellsToMove[(i, j1, j2)] = None

        if downLeft == downRight == '.': return True

        if '#' in (downLeft, downRight): return False

        if downLeft == '.': return canMoveDown(i+1, j2, j2+1)
        elif downRight == '.': return canMoveDown(i+1, j1-1, j1)
        else:
            if downLeft == '[': return canMoveDown(i+1, j1, j2) 
            else: return canMoveDown(i+1, j1-1, j1) and canMoveDown(i+1, j2, j2+1)

    downCell = Map[row+1][col]

    if downCell == '#': 
        return row, col

    elif downCell == '.':
        Map[row+1][col] = '@'
        Map[row][col] = '.'
        return row+1, col

    if downCell == '[' and canMoveDown(row+1, col, col+1):
        for i, j1, j2 in sorted(cellsToMove.keys(), reverse=True):
            Map[i+1][j1], Map[i+1][j2] = Map[i][j1], Map[i][j2]
            Map[i][j1] = Map[i][j2] = '.'

        Map[row+1][col] = '@'
        Map[row][col] = '.'

        row += 1

    else:
        cellsToMove.clear()

        if downCell == ']' and canMoveDown(row+1, col-1, col):
            for i, j1, j2 in sorted(cellsToMove.keys(), reverse=True):
                Map[i+1][j1], Map[i+1][j2] = Map[i][j1], Map[i][j2]
                Map[i][j1] = Map[i][j2] = '.'

            Map[row+1][col] = '@'
            Map[row][col] = '.'

            row += 1

    return row, col

def moveUp2(Map, row, col):
    cellsToMove = {}

    def canMoveUp(i, j1, j2):
        nonlocal Map, cellsToMove

        upLeft, upRight = Map[i-1][j1], Map[i-1][j2]

        cellsToMove[(i, j1, j2)] = None

        if upLeft == upRight == '.': return True

        if '#' in (upLeft, upRight): return False

        if upLeft == '.': return canMoveUp(i-1, j2, j2+1)
        elif upRight == '.': return canMoveUp(i-1, j1-1, j1)
        else:
            if upLeft == '[': return canMoveUp(i-1, j1, j2) 
            else: return canMoveUp(i-1, j1-1, j1) and canMoveUp(i-1, j2, j2+1)

    upCell = Map[row-1][col]

    if upCell == '#': 
        return row, col

    elif upCell == '.':
        Map[row-1][col] = '@'
        Map[row][col] = '.'
        return row-1, col

    if upCell == '[' and canMoveUp(row-1, col, col+1):
        for i, j1, j2 in sorted(cellsToMove.keys()):
            Map[i-1][j1], Map[i-1][j2] = Map[i][j1], Map[i][j2]
            Map[i][j1] = Map[i][j2] = '.'

        Map[row-1][col] = '@'
        Map[row][col] = '.'

        row -= 1

    else:
        cellsToMove.clear()

        if upCell == ']' and canMoveUp(row-1, col-1, col):
            for i, j1, j2 in sorted(cellsToMove.keys()):
                Map[i-1][j1], Map[i-1][j2] = Map[i][j1], Map[i][j2]
                Map[i][j1] = Map[i][j2] = '.'

            Map[row-1][col] = '@'
            Map[row][col] = '.'

            row -= 1

    return row, col

for index, move in enumerate(Moves):
    match move:
        case '^': subRow2, subCol2 = moveUp2(Map2, subRow2, subCol2)
        case 'v': subRow2, subCol2 = moveDown2(Map2, subRow2, subCol2)
        case '<': subRow2, subCol2 = moveLeft2(Map2, subRow2, subCol2)
        case '>': subRow2, subCol2 = moveRight2(Map2, subRow2, subCol2)
        case _: pass

result2 = sum( 100 * row + col for row, col in product(range(len(Map2)), range(len(Map2[0]))) if Map2[row][col] == '[' )

print(result2)