# DAY 19

import re
from collections import defaultdict
from functools import lru_cache

with open('input19.txt') as f:
    towels = f.readline().strip().split(', ')
    
    f.readline()

    onsens = [ line.strip() for line in f ]

def getReachable(onsen):
    global towels

    intervals = [ (m.start(), m.start() + len(towel)) for towel in towels for m in re.finditer(f'(?={towel})', onsen) ]

    reachable = defaultdict(set)

    for interval in intervals:
        reachable[interval[1]].add(interval[0])

    return reachable

def wasyReachable(length, reachable):

    '''
    @lru_cache(maxsize=None)
    def isReachable(index):
        nonlocal reachable

        if index == 0:
            return True

        for start in reachable[index]:
            if isReachable(start):
                return True

        return False
    '''

    @lru_cache(maxsize=None)
    def countWays(index):
        nonlocal reachable

        if index < 0:
            return 0

        if index == 0:
            return 1

        return sum( countWays(start) for start in reachable[index] )

    return countWays(length)

reachables = [ getReachable(onsen) for onsen in onsens ]

ways = [ wasyReachable(len(onsen), reachables[index]) for index, onsen in enumerate(onsens) ]

result1, result2 = sum( int(w > 0) for w in ways ), sum(ways)

print(result1, result2)