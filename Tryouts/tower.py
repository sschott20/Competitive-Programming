import sys

numBricks = int(sys.stdin.readline()[:-1])

brickWidths = [int(i) for i in sys.stdin.readline()[:-1].split()]

curTop = -1

numTowers = 0

for brick in brickWidths:
    if brick > curTop:
        numTowers += 1
    
    curTop = brick

print(numTowers)