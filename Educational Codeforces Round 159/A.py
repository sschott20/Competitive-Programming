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
    for i in test:
        if i == "0":
            return "YES"
    return "NO"


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(insr())
        continue
    for test in tests:
        print(solve(test))
