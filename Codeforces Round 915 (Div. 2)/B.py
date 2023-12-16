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
    n, edges = test
    ret = [0 for i in range(n)]
    for edge in edges:
        ret[edge[0] - 1] += 1
        ret[edge[1] - 1] += 1

    acc = 0
    for j in ret:
        if j == 1:
            acc += 1

    return (acc + 1) // 2


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        n = inp()
        test = []
        for j in range(n - 1):
            test.append(inlt())
        tests.append((n, test))

    for test in tests:
        print(solve(test))
