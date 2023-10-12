import sys

cards = []

for i in range(4):
    cards += sys.stdin.readline()[:-1].split()

validSets = []

for i in range(12):
    for j in range(i+1, 12):
        for k in range(j+1, 12):
            isSet = True
            for x,y,z, in zip(cards[i], cards[j], cards[k]):
                if x == y and y == z and z == x:
                    continue
                if x != y and y != z and z != x:
                    continue
                
                isSet = False
                break

            if isSet:
                validSets.append([i,j,k])


if len(validSets) == 0:
    print('no sets')
else:
    for i,j, k in validSets:
        print(f'{i+1} {j+1} {k+1}')