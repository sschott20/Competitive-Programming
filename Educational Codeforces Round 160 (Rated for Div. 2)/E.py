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


def print_matrix(matrix):
    for row in matrix:
        print(row)


def solve(test):
    m, a, b = test
    print_matrix(m)
    print(a)
    print(b)
    row_sum = []
    col_sum = []
    for row in m:
        row_sum.append(sum(row))
    for col in range(len(m[0])):
        col_sum.append(sum([row[col] for row in m]))
    print(row_sum)
    print(col_sum)
    d = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            d[(i, j)] = m[i][j]
    return


if __name__ == "__main__":
    tests = []
    n, m = inlt()
    m = []
    test = []
    for i in range(n):
        m.append(inlt())
    test.append(m)
    test.append(inlt())
    test.append(inlt())
    tests.append(test)
    for test in tests:
        print(solve(test))
