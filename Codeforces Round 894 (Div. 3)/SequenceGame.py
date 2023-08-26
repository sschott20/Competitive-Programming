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
    final = []
    for i in range(len(test)):
        if i == 0 or test[i - 1] <= test[i]:
            final.append(test[i])
        else:
            m = min(test[i - 1] - 1, test[i] - 1)
            final.append(max(m, 1))
            final.append(test[i])

    print(len(final))
    print(" ".join(map(str, final)))
    return final


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())

    for test in tests:
        solve(test)