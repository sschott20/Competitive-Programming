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
    a, b, xk, yk, xq, yq = test
    acc = 0

    delta = [(a, b), (-a, b), (a, -b), (-a, -b), (b, a), (-b, a), (b, -a), (-b, -a)]
    if a == b:
        delta = [(a, b), (-a, b), (a, -b), (-a, -b)]
    king = []
    queen = []
    for d in delta:
        king.append([xk + d[0], yk + d[1]])
        queen.append([xq + d[0], yq + d[1]])
    for k in king:
        if k in queen:
            acc += 1

    return acc


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        a, b = inlt()
        xk, yk = inlt()
        xq, yq = inlt()
        tests.append((a, b, xk, yk, xq, yq))

    for test in tests:
        print(solve(test))
