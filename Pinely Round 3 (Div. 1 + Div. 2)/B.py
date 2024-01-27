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
    k = 2
    while k < 2 * max(test):
        s = set()
        for i in test:
            if len(s) > 2:
                break
            s.add(i % k)

        if len(s) == 2:
            return k
        k *= 2
    return k


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())
    for test in tests:
        print(solve(test))
