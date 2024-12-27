# DAY 11

from collections import defaultdict

def transform(x):
    if x == 0: return (1,)

    strX = str(x)

    if (LenStrX := len(strX)) % 2 == 0:
        LenStrX_2 = LenStrX // 2
        return (int(strX[:LenStrX_2]), int(strX[LenStrX_2:]))

    return (x * 2024,)

def getNewStones(stones):
    newStones = defaultdict(int)

    for stone, freq in stones.items():
        for newStone in transform(stone):
            newStones[newStone] += freq

    return newStones

with open('input11.txt') as f:
    stones = defaultdict(int, { x : 1 for x in map(int, f.readline().strip().split()) })

for i in range(75):
    stones = getNewStones(stones)

result = sum( freq for stone, freq in stones.items() )

print(result)