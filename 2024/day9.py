# DAY 9

from heapq import heappush, heappop

with open('input9.txt') as f:
    line = f.readline().strip()

emptyLists = [ ['.'] * i for i in range(0, 10) ]

disk, disk2, blockId, digits = [], [], 0, 0

for i, d in enumerate(line):
    if d == '0':
        continue

    d = int(d)

    if i % 2:
        disk.extend(emptyLists[d]); disk2.append(['.', d]);
    else:
        disk.extend([blockId] * d); disk2.append([blockId, d])

        blockId += 1
        digits += d

left, right, index = 0, len(disk) - 1, 0

while index < digits:
    if disk[left] == '.':
        while disk[right] == '.': 
            right -= 1

        disk[left] = disk[right]
        right -= 1
    
    left += 1
    index += 1

result1 = sum( i * disk[i] for i in range(digits) )

print(result1)

#-------------------------------------------------------

diskFlattened = [ d for d, i in disk2 for j in range(i) ]

emptyPositions = { i : [] for i in range(1, 10) }
index, L = 0, len(diskFlattened)
inEmpty, start = False, -1

while index < L:
    if diskFlattened[index] == '.':
        if not inEmpty:
            inEmpty, start = True, index
    else:
        if inEmpty:
            heappush(emptyPositions[index - start], start)
            inEmpty = False
    index += 1

index = L

for d, length in reversed(disk2):
    index -= length

    if d != '.':
        try:
            position, emptyLength = min(((emptyPositions[i][0], i) for i in range(length, 10) if len(emptyPositions[i])), key = lambda t : t[0])
        except ValueError:
            continue

        if position > index:
            continue

        diskFlattened[position : position + length] = [d] * length
        diskFlattened[index : index + length] = '.' * length

        heappop(emptyPositions[emptyLength])

        if emptyLength != length:
            heappush(emptyPositions[emptyLength - length], position + length)

result2 = sum( i * v for i, v in enumerate(diskFlattened) if v != '.' )

print(result2)