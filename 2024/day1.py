# DAY 1

listLeft, listRight = [], []

with open("input1.txt") as f:
	for line in f:
		left, right = line.split('   ')
		listLeft.append(int(left))
		listRight.append(int(right))

listLeft.sort()
listRight.sort()

s = sum( abs(listLeft[i] - listRight[i]) for i in range(len(listLeft)) )

print(s)

#-----------------------------------------------------------------------

from collections import Counter

CounterLeft, CounterRight = Counter(listLeft), Counter(listRight)

score = sum( i * CounterLeft[i] * CounterRight[i] for i in CounterLeft.keys() )

print(score)