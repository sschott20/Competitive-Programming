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
    n, P, l, t = test
    num_tasks = floor((n - 1) / 7) + 1
    if num_tasks * t + ceil(num_tasks / 2) * l >= P:
        num_days = ceil(P / (l + 2 * t))

        return n - num_days
    else:
        num_pts = num_tasks * t + ceil(num_tasks / 2) * l
        extra_days = ceil((P - num_pts) / (l))
        # print()
        return n - ceil(num_tasks / 2) - extra_days


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(inlt())
    for test in tests:
        print(solve(test))
