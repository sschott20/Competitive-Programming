import sys
from math import *

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


def solve(x, s):
    s = "".join(s)

    for i in range(0, 15):
        if s in "".join(x):
            return i
        else:
            x = x + x
        if len(x) > 4 * len(s) and i >= 3:
            return -1
    return -1


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inlt()
        x, s = insr(), insr()
        tests.append([x, s])
    for test in tests:
        print(solve(test[0], test[1]))
