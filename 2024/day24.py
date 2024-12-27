# DAY 24

from collections import defaultdict

OR = lambda a, b : a | b
AND = lambda a, b : a & b
XOR = lambda a, b : a ^ b

with open('input24.txt') as f:
    gatesParse, wires, outputs, inputs,  = False, dict(), dict(), defaultdict(list)

    for line in f:
        line = line.strip()

        if len(line) == 0:
            gatesParse = True
            continue

        if gatesParse:
            inWires, outWire = line.split(' -> ')

            if ' OR ' in inWires:
                left, right = inWires.split(' OR ')
                outputs[outWire] = (left, right, OR)

            elif ' AND ' in inWires:
                left, right = inWires.split(' AND ')
                outputs[outWire] = (left, right, AND)

            else:
                left, right = inWires.split(' XOR ')
                outputs[outWire] = (left, right, XOR)

            inputs[left].append(outWire)
            inputs[right].append(outWire)

            if outWire.startswith('z'):
                inputs[outWire]

            if left not in wires:
                wires[left] = None

            if right not in wires:
                wires[right] = None

        else:
            wire, value = line.split(':')
            wires[wire] = int(value)

inputWires = set([ wire for wire, value in wires.items() if value != None ])

def run(currentInputs):
    global wires

    while currentInputs:
        newInputs = set()
        
        for wire in currentInputs:
            for outWire in inputs[wire]:
                left, right, gate = outputs[outWire]
                leftValue, rightValue = wires[left], wires[right]

                if None not in (leftValue, rightValue):
                    wires[outWire] = gate(leftValue, rightValue)
                    newInputs.add(outWire)

        currentInputs = newInputs.copy()

    result = int('0b' + ''.join(reversed([str(wires[wire]) for wire in sorted(wire for wire in wires if wire.startswith('z') ) ])), 2)

    return result

result1 = run(inputWires)

print(result1)

#----------------------------------------------------------------------------------

# Not my code...
# Visualizing the cirsuit helps figure it out...

from operator import xor as XOR, or_ as OR, and_ as AND

for l in open('input24.txt'):
    try:    a,x,b,_,c = l.split(); exec(f'{c}=lambda:{x}({a}(),{b}())')
    except: exec(l.replace(':', '=lambda:'))

print(sum(eval(f'z{i:02}()<<{i}') for i in range(46)))


lines = [ l.split() for l in open('input24.txt') if '->' in l ]

r = lambda c, y: any(y == x and c in (a, b) for a, x, b, _, _ in lines)

print(*sorted(c for a, x, b, _, c in lines if
    x == "XOR" and all(d[0] not in 'xyz' for d in (a, b, c)) or
    x == "AND" and not "x00" in (a, b) and r(c, 'XOR') or
    x == "XOR" and not "x00" in (a, b) and r(c, 'OR') or
    x != "XOR" and c[0] == 'z' and c != "z45"), sep=',')