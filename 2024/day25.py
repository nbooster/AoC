# DAY 25

with open('input25.txt') as f:
    Locks, Keys, current, height = [], [], [], 7

    for line in f:
        line = line.strip()

        if len(line) == 0:
            continue

        if line == '.....' and len(current) == height - 1:
            Locks.append(current + [line])
            current.clear()

        elif line == '#####' and len(current) == height - 1:
            Keys.append(current + [line])
            current.clear()

        else:
            current.append(line)

for index, lock in enumerate(Locks):
    Locks[index] = tuple( sum(1 for i in range(len(lock)) if lock[i][j] == '#') - 1 for j in range(len(lock[0])) )

for index, key in enumerate(Keys):
    Keys[index] = tuple( sum(1 for i in range(len(key)) if key[i][j] == '#') - 1 for j in range(len(key[0])) )

def match(key, lock):
    return all( key[index] + lock[index] <= height - 2 for index in range(len(key)) )

result1 = sum( int(match(key, lock)) for key in Keys for lock in Locks )

print(result1)