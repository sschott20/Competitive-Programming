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
    a, b = test
    ev = []
    for i in range(len(a)):
        ev.append([a[i] + b[i], i])
    ev.sort(reverse=True)
    for i in range(len(ev)):
        if i % 2 == 0:
            a[ev[i][1]] = a[ev[i][1]] - 1
            b[ev[i][1]] = 0
        else:
            a[ev[i][1]] = 0
            b[ev[i][1]] = b[ev[i][1]] - 1
    return sum(a) - sum(b)


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append([inlt(), inlt()])
    for test in tests:
        print(solve(test))
