# DAY 14

# run it with pypy for faster execution

with open('input14.txt') as f:
    positions, velocities = [], []

    for line in f:
        pos, vel = line.strip().split(' ')
        _, pos = pos.split('=')
        _, vel = vel.split('=')
        x, y = pos.split(',')
        vx, vy = vel.split(',')
        
        positions.append([int(x), int(y)])
        velocities.append((int(vx), int(vy)))

seconds, width, height = 10000, 101, 103

from collections import Counter
from time import sleep

for s in range(seconds):
    for index, pos in enumerate(positions):
        x, y = pos
        vx, vy = velocities[index]

        positions[index] = [( x + vx ) % width, ( y + vy ) % height]

    C = Counter(tuple(pos) for pos in positions)
    
    Map = [['.'] * width for _ in range(height)]
    for pos, freq in C.items():
        Map[pos[1]][pos[0]] = '#' #freq #part1

    for i, row in enumerate(Map):
        if '#' * 8 in ''.join(row):
            print(s + 1)
            for row in Map: print(''.join(row))
            exit()

#part1
'''from itertools import product

sum1 = 0
for pos in product(range(width // 2), range(height // 2)):
    sum1 += C[pos]

sum2 = 0
for pos in product(range(width // 2), range(height // 2 + 1, height)):
    sum2 += C[pos]

sum3 = 0
for pos in product(range(width // 2 + 1, width), range(height // 2)):
    sum3 += C[pos]

sum4 = 0
for pos in product(range(width // 2 + 1, width), range(height // 2 + 1, height)):
    sum4 += C[pos]

result1 = sum1 * sum2 * sum3 * sum4

print(result1)'''