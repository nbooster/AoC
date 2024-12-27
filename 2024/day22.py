# DAY 22

from time import time

start = time()

with open('input22.txt') as f:
    numbers = [ int(line.strip()) for line in f ]

def nextSecretNumber(x):
    x = (x ^ (x * 64)) % 16777216
    x = (x ^ int(x // 32)) % 16777216
    return (x ^ (x * 2048)) % 16777216

def nextNSecretNumber(x, N):
    for _ in range(N):
        x = nextSecretNumber(x)

    return x

N = 2000

result1 = sum( nextNSecretNumber(x, N) for x in numbers )

print(result1, time() - start)

#------------------------------------------------------------

def getDiffsToPrices(x, N):
    prices = [ x % 10 ]

    for _ in range(N):
        x = nextSecretNumber(x)
        prices.append(x % 10)

    diffs = [ None ] + [ prices[i] - prices[i - 1] for i in range(1, N) ]
    
    DiffsToPrices = dict()

    for i in range(4, len(diffs)):
        key = tuple(diffs[i-3 : i+1])

        if key not in DiffsToPrices:
            DiffsToPrices[key] = prices[i]

    return DiffsToPrices

start = time()

Dicts = [ getDiffsToPrices(secret, N) for secret in numbers ]

allDiffs = set( diff for d in Dicts for diff in d.keys() )

result2 = max( sum( d.get(diff, 0) for d in Dicts ) for diff in allDiffs )

print(result2, time() - start)