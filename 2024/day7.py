# DAY 7

# run it with pypy for faster execution

def genbin1(n, bs = ''):
    if n:
        yield from genbin1(n-1, bs + '+')
        yield from genbin1(n-1, bs + '*')
    else:
        yield bs

def check1(equation, operations, resultArg):
    result = equation[0]

    for i in range(1, len(operations)):
        if operations[i] == '+':
            result += equation[i]
        else:
            result *= equation[i]

        #if result > resultArg:
         #   return False

    return result == resultArg

with open('input7.txt') as f:
    calibrations, lengths = [], set()

    for line in f:
        value, equation = line.strip().split(':')
        equation = tuple(map(int, equation.split()))
        calibrations.append((int(value), equation))
        lengths.add(len(equation))

from collections import defaultdict

Combs = defaultdict(list)

for length in lengths:
    for operation in genbin1(length):
        Combs[length].append(operation)

s = 0

for result, equation in calibrations:
    for operation in Combs[len(equation)]:
        if check1(equation, operation, result):
            s += result
            break

print(s)

#---------------------------------------------------------------------------

import math, time

def concat(x, y):
    '''if y != 0:
        a = math.floor(math.log10(y))
    else:
        a = -1'''

    return int(x*10**(1+math.floor(math.log10(y)))+y)

def genbin2(n, bs = ''):
    if n:
        yield from genbin2(n-1, bs + '+')
        yield from genbin2(n-1, bs + '*')
        yield from genbin2(n-1, bs + '|')
    else:
        yield bs

def check2(equation, operations, resultArg):
    result = equation[0]

    for i in range(1, len(operations)):
        if (op := operations[i]) == '+':
            result += equation[i]
        elif op == '*':
            result *= equation[i]
        else:
            result = concat(result, equation[i])#int(str(result) + str(equation[i]))

        if result > resultArg:
            return False

    return result == resultArg

'''start = time.time()

Combs = defaultdict(list)

for length in lengths:
    for operation in genbin2(length):
        Combs[length].append(operation)

s = 0

for result, equation in calibrations:
    for operation in Combs[len(equation)]:
        if check2(equation, operation, result):
            s += result
            break

end = time.time()

print(s, end - start)'''

#------------------------------------------------------------------------------------------------
# not my solution (same logic but better implemented) but improved by me (time cut in half)

from operator import add, mul

start = time.time()

cat = concat #lambda x,y: int(str(x) + str(y))

ans = 0

for line in open('input7.txt'):
    tgt, x, *Y = map(int, line.replace(':', '').split())

    X = [x]

    for y in Y:
        X = [ op(x,y) for x in X if x <= tgt for op in (add, mul, cat) ] #remove concat for part 1

    if tgt in X: 
        ans += tgt

end = time.time()

print(ans, end-start)