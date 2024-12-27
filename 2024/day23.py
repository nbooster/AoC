# DAY 23

from collections import defaultdict
from itertools import combinations

letter = 't'

with open('input23.txt') as f:
    D = defaultdict(set)

    for line in f:
        a, b = line.strip().split('-')

        D[a].add(b)
        D[b].add(a)

triplets = set()

for key in D:
    if key.startswith(letter):
        for a, b in combinations(D[key], 2):
            if b in D[a] or a in D[b]:
                triplets.add(tuple(sorted([key, a, b])))

print(len(triplets))

#-----------------------------------------------------------

from time import time

start = time()

maxClique = tuple()

#Bron–Kerbosch with pivoting
def bronkp(r, p, x):
    global maxClique

    if len(p) == len(x) == 0:
        if len(r) > len(maxClique):
            maxClique = tuple(r)
        
        return

    for vertex in p.difference(D[(p.union(x)).pop()]):
        neighbors = D[vertex]

        bronkp(r.union(set([vertex])), p.intersection(neighbors), x.intersection(neighbors))

        p.remove(vertex)
        x.add(vertex)

bronkp(set(), set(D.keys()), set())

print(','.join(sorted(maxClique)), time() - start)

# or use this:
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.clique.find_cliques.html