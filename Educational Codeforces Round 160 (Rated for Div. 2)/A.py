import sys
from math import *
import collections

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
    left = []
    right = test
    for t in test:
        left.append(test.pop(0))
        if int("".join(left)) < int("".join(right)) and right[0] != "0":
            return str(int("".join(left))) + " " + str(int("".join(right)))
    return "-1"


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(insr())

    for test in tests:
        print(solve(test))
