# DAY 5

from collections import defaultdict
from itertools import islice

Rules, Updates, wrongUpdates = defaultdict(list), [], []

def isValid(update, Rules, wrongUpdates):
    for index, a in enumerate(update):
        for b in islice(update, index + 1, len(update)):
            if a in Rules[b]:
                wrongUpdates.append(update)
                return False

    return True

with open('input5.txt') as f:
    for line in f:
        line = line.strip()
        if '|' in line:
            a, b = line.split('|')
            Rules[a].append(b)

        else:
            if len(line) > 0:
                Updates.append(line.split(','))

s = sum( int(update[len(update) // 2]) for update in Updates if isValid(update, Rules, wrongUpdates) )

print(s)

#--------------------------------------------------------------------------------------------------------

for u in range(len(wrongUpdates)):
    for i in range(len(wrongUpdates[u])):
        for j in range(i + 1, len(wrongUpdates[u])):
            if wrongUpdates[u][i] in Rules[wrongUpdates[u][j]]:
                wrongUpdates[u][i], wrongUpdates[u][j] = wrongUpdates[u][j], wrongUpdates[u][i]

ss = sum( int(update[len(update) // 2]) for update in wrongUpdates )

print(ss)