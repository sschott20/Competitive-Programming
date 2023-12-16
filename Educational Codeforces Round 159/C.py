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
    x = 0
    diffs = []
    acc = 0
    test.sort()

    M = max(test)

    # diffs is a list of the differences between the elements of test
    for i in range(len(test) - 1):
        diff = abs(test[i + 1] - test[i])
        x = gcd(x, diff)

    if x == 0:
        return 1

    for i in test:
        acc += int((M - i) / x)

    cur = M
    d = set(test)
    for i in range(len(test)):
        if cur in d:
            cur -= x
        else:
            return i + acc
    return len(test) + acc

    return acc


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())

    for test in tests:
        print(solve(test))
