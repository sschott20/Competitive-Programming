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


def solve(test):
    rows = len(test[0]) * min(test[0]) + sum(test[1])
    cols = len(test[0]) * min(test[1]) + sum(test[0])
    return min(rows, cols)


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append([inlt(), inlt()])
        continue
    for test in tests:
        print(solve(test))
