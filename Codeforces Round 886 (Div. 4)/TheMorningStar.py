import sys
from math import comb, factorial

input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


def num_pairs(points):
    # find number of pairs that have have the same point[0]
    diffx = []
    diffy = []
    for point in points:
        diffx.append(point[1] - point[0])
        diffy.append(point[1] + point[0])
    # print(diffx, diffy)

    xlist, ylist = list(zip(*points))
    pairs = 0
    curx = 1
    cury = 1
    dx = 1
    dy = 1

    for i in range(len(points) - 1):
        if ylist[i] == ylist[i + 1]:
            cury += 1
        else:
            pairs += cury * (cury -1)
            cury = 1

        if xlist[i] == xlist[i + 1]:
            curx += 1
        else:
            pairs += curx * (curx - 1)
            curx = 1

        if diffx[i] == diffx[i + 1]:
            dx += 1
        else:
            pairs += dx * (dx - 1)
            dx = 1

        if diffy[i] == diffy[i + 1]:
            dy += 1
        else:
            pairs += dy * (dy - 1)
            dy = 1

    pairs += curx * (curx - 1)
    pairs += cury * (cury - 1)
    pairs += dx * (dx - 1)
    pairs += dy * (dy - 1)

    return pairs


if __name__ == "__main__":
    numtests = inp()
    tests = []
    for i in range(numtests):
        numpoints = inp()
        points = []

        for j in range(numpoints):
            points.append(inlt())

        tests.append(points)

    for test in tests:
        print(num_pairs(test))
