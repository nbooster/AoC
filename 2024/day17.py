# DAY 17

# run it with pypy for faster execution

with open('input17.txt') as f:
    _, A = f.readline().strip().split(':')
    _, B = f.readline().strip().split(':')
    _, C = f.readline().strip().split(':')
    A, B, C = int(A), int(B), int(C)

    f.readline()

    _, program = f.readline().strip().split(':')
    program = list(map(int, program.split(',')))

def combo(op):
    return op if 0 <= op <= 3 else [A, B, C][op - 4]

IP, output = 0, []

while IP < len(program):
    opc, ope = program[IP : IP + 2]
    jmp = False

    match opc:
        case 0:
            A = int(A / (2**combo(ope)))

        case 1:
            B ^= ope

        case 2:
            B = combo(ope) % 8

        case 3:
            if A == 0: 
                IP += 1
            
            else: 
                IP, jmp = ope, True

        case 4:
            B ^= C

        case 5:
            output.append(str(combo(ope) % 8))

        case 6:
            B = int(A / (2**combo(ope)))

        case 7:
            C = int(A / (2**combo(ope)))

        case _:
            pass

    if not jmp:
        IP += 2

result1 = ','.join(output)

print(result1)

#---------------------------------------------------------------

from time import time
from itertools import product

def programCompute(x):
    X = ( A % 8 )
    return ( ( A >> ( X ^ 3 ) ) ^ X ^ 6 ) % 8, X

start = time()

possible = [ ['000'] ]

for output in reversed(program):
    values = set()

    for t in product(*possible[-3:]):
        number = '0b' + ''.join(t)
        
        for A in range(int(number + '000', 2), int(number + '111', 2) + 1):
            if ( result := programCompute(A) )[0] == output:
                values.add(str(bin(result[1]))[2:].zfill(3))

    possible.append(sorted(values))

for t in product(*possible):
    A = number = int('0b' + ''.join(t), 2)
    output = []

    while A:        
        output.append(programCompute(A)[0])
        A >>= 3
        
    if output == program:
        print(number, time() - start)
        break