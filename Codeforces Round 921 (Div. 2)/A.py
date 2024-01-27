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
    n, k = test
    sub = [97 + i for i in range(k)]
    sub = "".join(map(chr, sub))
    ret = ""
    for i in range(n):
        ret += sub

    return ret


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        n, k = inlt()
        tests.append([n, k])
        continue
    for test in tests:
        print(solve(test))
