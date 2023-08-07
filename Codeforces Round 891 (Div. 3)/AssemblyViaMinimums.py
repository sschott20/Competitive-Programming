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
    arr = []
    n, l = test
    acc = 0
    l.sort()
    while n > 1:
        # print(acc, n, arr)
        arr.append(l[acc])
        acc += n - 1
        n -= 1
    arr.append(max(arr))
    arr = [str(x) for x in arr]
    arr = " ".join(arr)
    return arr


if __name__ == "__main__":
    tests = []
    num_tests = inp()

    for i in range(num_tests):
        tests.append([inp(), sorted(inlt())])

    for test in tests:
        print(solve(test))
