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
    zeroes = 0
    ones = 0

    for i in test:
        if i == "0":
            zeroes += 1
        else:
            ones += 1
    if zeroes == ones:
        return 0
    if len(test) == 1:
        return 1

    for i in range(len(test)):
        if test[i] == "1":
            zeroes -= 1
        else:
            ones -= 1
            # if zeroes <= 0:
            #     for j in range(i, len(test)):
            #         if test[j] == "1":
            #             ones -= 1
        if zeroes < 0 or ones < 0:
            return len(test) - i


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(insr())

    for test in tests:
        print(solve(test))
