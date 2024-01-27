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
    x, n = test
    for i in range(floor(x / n), 0, -1):
        tmp = x - n * i
        if tmp % i == 0:
            return i
    return


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    # n(n+1)/2
    for i in range(num_tests):
        tests.append(inlt())
        continue
    for test in tests:
        print(solve(test))
