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
    d = {}
    acc = 0
    ret = set()
    for t in test:
        tmp = ord(t) - ord("A") + 1
        if tmp in d:
            d[tmp] += 1
        else:
            d[tmp] = 1
        if d[tmp] >= tmp:
            ret.add(tmp)
    return len(ret)


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(insr())
    for test in tests:
        print(solve(test))
