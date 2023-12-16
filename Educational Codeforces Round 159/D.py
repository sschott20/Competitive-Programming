import sys
from math import *
from collections import defaultdict

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


def solve(test):
    return


if __name__ == "__main__":
    tests = []
    q, num_tests = inlt()
    visits = defaultdict(set)
    path = insr()
    loc = (0, 0)
    visits[loc].add(0)
    seq = [loc]
    for i, p in enumerate(path):
        if p == "U":
            loc = (loc[0], loc[1] + 1)
        elif p == "D":
            loc = (loc[0], loc[1] - 1)
        elif p == "L":
            loc = (loc[0] - 1, loc[1])
        elif p == "R":
            loc = (loc[0] + 1, loc[1])
        visits[loc].add(i + 1)
        seq.append(loc)

    for i in range(num_tests):
        tests.append(inlt())

    for test in tests:
        ret = "NO"
        x, y, l, r = test
        if (x, y) in visits:
            t = visits[(x, y)]
            for i in t:
                if i <= l and i >= r:
                    ret = "YES"
                    break
        start = seq[l - 1]
        end = seq[r - 1]
        delta = (x - start[0], y - start[1])
        if (end[0] - delta[0], end[1] - delta[1]) in visits:
            tmp = visits[(end[0] - delta[0], end[1] - delta[1])]
            for i in tmp:
                if l < i < r:
                    ret = "YES"
                    break
        print(ret)
