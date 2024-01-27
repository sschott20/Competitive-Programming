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
    spl = [i for i in range(1, n + 1)]
    front = spl[n - k - 1 :]
    back = spl[: n - k - 1]
    back.reverse()
    ret = front + back

    return " ".join(map(str, ret))


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(inlt())

    for test in tests:
        print(solve(test))
